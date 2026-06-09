from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Label
from textual.containers import Center, Vertical

from models.user import User


class SettingsView(Screen):
    """
    Responsável pela formação da Tela de Configuerações do Usuário
    """

    def __init__(self, user: User) -> None:
        super().__init__()
        self.current_user = user

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="auth-box"):
                yield Static("Configurações", id="title")
                yield Label(self.current_user.user_name, id="message")

                yield Button("Alterar Nome",    id="btn-name")
                yield Button("Alterar E-mail",  id="btn-email")
                yield Button("Alterar Senha",   id="btn-pw")
                yield Button("Deletar Conta",   id="btn-delete", variant="error")
                yield Button("Voltar",              id="btn-back")

    def on_screen_resume(self) -> None:
        self.query_one("#message", Label).update(
            f"{self.current_user.user_name}  ·  {self.current_user.email}"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        bid = event.button.id

        if bid == "btn-back":
            self.app.pop_screen()
            return

        if bid == "btn-name":
            from ui.screens.config.change_name import ChangeNameView
            self.app.push_screen(ChangeNameView(self.current_user))
            return

        if bid == "btn-email":
            from ui.screens.config.change_email import ChangeEmailView
            self.app.push_screen(ChangeEmailView(self.current_user))
            return

        if bid == "btn-pw":
            from ui.screens.config.change_password import ChangePasswordView
            self.app.push_screen(ChangePasswordView(self.current_user))
            return

        if bid == "btn-delete":
            from ui.screens.config.delete_account import DeleteAccountView
            self.app.push_screen(DeleteAccountView(self.current_user))
