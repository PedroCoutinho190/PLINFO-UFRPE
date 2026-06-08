import asyncio, re
from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label
from textual.containers import Center, Vertical, Horizontal
from textual            import work

from models.user import User
from services.user_config_service import UserConfigService
from database.__database  import db
from utils.email_service  import email_service
from utils.password_toggle import toggle_password


def _clean(t): return re.sub(r"\x1b\[[0-9;]*m", "", str(t))


class ChangePasswordView(Screen):
    """
    Responsável pela Formação da Screen da Troca de senha
    """

    def __init__(self, user: User) -> None:
        super().__init__()
        self.current_user = user
        self.config = UserConfigService(db, user)

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="auth-box"):
                yield Static("Alterar Senha", id="title")

                with Horizontal(id="password-row"):
                    yield Input(placeholder="Nova senha...", id="password", password=True)
                    yield Button("Mostrar", id="toggle-pw")

                with Horizontal(id="confirm-row"):
                    yield Input(placeholder="Confirme a nova senha...", id="confirm", password=True)
                    yield Button("Mostrar", id="toggle-confirm")

                yield Label("", id="message")
                yield Button("Salvar", id="btn-save", variant="primary")
                yield Button("Voltar", id="btn-back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        bid = event.button.id

        if bid == "toggle-pw":
            toggle_password(self, "password", "toggle-pw")
            return

        if bid == "toggle-confirm":
            toggle_password(self, "confirm", "toggle-confirm")
            return

        if bid == "btn-back":
            self.app.pop_screen()
            return

        if bid == "btn-save":
            pw  = self.query_one("#password", Input).value.strip()
            cf  = self.query_one("#confirm",  Input).value.strip()
            ok, msg = self.config.validate_password(pw, cf)
            if not ok:
                self.query_one("#message", Label).update(_clean(msg))
                return
            self._pending_pw = pw
            self.query_one("#message", Label).update("Enviando código de verificação...")
            self._verify(self.current_user.email, pw)

    @work
    async def _verify(self, email: str, new_pw: str) -> None:
        from ui.modals.verify_code import VerifyCodeModal
        loop = asyncio.get_event_loop()
        code = await loop.run_in_executor(None, email_service.send_code, email)
        if not code:
            self.query_one("#message", Label).update("Erro ao enviar e-mail. Verifique o .env")
            return
        self.query_one("#message", Label).update("")
        ok = await self.app.push_screen_wait(VerifyCodeModal(email, code))
        if ok:
            self.config.update_password(new_pw)
            self.app.notify("Senha alterada com sucesso!")
            self.app.pop_screen()
        else:
            self.query_one("#message", Label).update("Verificação cancelada.")
