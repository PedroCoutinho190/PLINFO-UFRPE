import asyncio
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


class DeleteAccountView(Screen):

    def __init__(self, user: User) -> None:
        super().__init__()
        self.current_user = user
        self.config = UserConfigService(db, user)

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="auth-box"):
                yield Static("Deletar Conta", id="title")
                yield Static(
                    "Esta ação é permanente e irreversível.",
                    classes="subtitle"
                )
                with Horizontal(id="password-row"):
                    yield Input(placeholder="Confirme sua senha...", id="password", password=True)
                    yield Button("Mostrar", id="toggle-pw")
                yield Label("", id="message")
                yield Button("Deletar minha conta", id="btn-delete", variant="error")
                yield Button("Cancelar", id="btn-back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        bid = event.button.id

        if bid == "toggle-pw":
            toggle_password(self, "password", "toggle-pw")
            return

        if bid == "btn-back":
            self.app.pop_screen()
            return

        if bid == "btn-delete":
            pw = self.query_one("#password", Input).value.strip()
            ok, msg = self.config.validate_delete(pw)
            if not ok:
                self.query_one("#message", Label).update(msg)
                self.query_one("#password", Input).add_class("invalid")
                return
            self.query_one("#message", Label).update("Enviando código de verificação...")
            self._verify(self.current_user.email)

    @work
    async def _verify(self, email: str) -> None:
        from ui.modals.verify_code import VerifyCodeModal
        loop = asyncio.get_event_loop()
        code = await loop.run_in_executor(None, email_service.send_code, email)
        if not code:
            self.query_one("#message", Label).update("Erro ao enviar e-mail. Verifique o .env")
            return
        self.query_one("#message", Label).update("")
        ok = await self.app.push_screen_wait(VerifyCodeModal(email, code))
        if ok:
            self.config.delete()
            self.app.notify("Conta deletada. Até logo!")
            # Volta pro login limpando toda a pilha
            while len(self.app.screen_stack) > 1:
                self.app.pop_screen()
        else:
            self.query_one("#message", Label).update("Verificação cancelada.")
