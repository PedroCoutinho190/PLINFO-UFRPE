import asyncio
from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label
from textual.containers import Center, Vertical
from textual            import work

from models.user import User
from services.user_config_service import UserConfigService
from database.__database  import db
from utils.email_service  import email_service


class ChangeEmailView(Screen):
    """
    Responsável pela Formação da Screen da Troca de E-mail
    """
    def __init__(self, user: User) -> None:
        super().__init__()
        self.current_user = user
        self.config = UserConfigService(db, user)

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="auth-box"):
                yield Static("Alterar E-mail", id="title")
                yield Static(
                    f"E-mail atual: {self.current_user.email}",
                    classes="subtitle"
                )
                yield Input(placeholder="Novo e-mail institucional...", id="email")
                yield Label("", id="message")
                yield Button("Salvar", id="btn-save", variant="primary")
                yield Button("Voltar", id="btn-back")

    def on_input_changed(self, event: Input.Changed) -> None:
        from utils.validations import Validation
        v = event.value.strip().lower()
        self.query_one("#message", Label).update("")
        if v:
            f = self.query_one("#email", Input)
            if Validation.validadion_email(v):
                f.remove_class("invalid")
            else:
                f.add_class("invalid")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-back":
            self.app.pop_screen()
            return

        if event.button.id == "btn-save":
            new_email = self.query_one("#email", Input).value.strip().lower()
            ok, err = self.config.validate_email(new_email)
            if not ok:
                self.query_one("#message", Label).update(err)
                self.query_one("#email", Input).add_class("invalid")
                return
            self._pending_email = new_email
            self.query_one("#message", Label).update("Enviando código de verificação...")
            self._verify(self.current_user.email, new_email)

    @work
    async def _verify(self, current_email: str, new_email: str) -> None:
        from ui.modals.verify_code import VerifyCodeModal
        loop = asyncio.get_event_loop()
        code = await loop.run_in_executor(None, email_service.send_code, current_email)
        if not code:
            self.query_one("#message", Label).update("Erro ao enviar e-mail. Verifique o .env")
            return
        self.query_one("#message", Label).update("")
        ok = await self.app.push_screen_wait(VerifyCodeModal(current_email, code))
        if ok:
            self.config.update_email(new_email)
            self.app.notify("E-mail alterado com sucesso!")
            self.app.pop_screen()
        else:
            self.query_one("#message", Label).update("Verificação cancelada.")
