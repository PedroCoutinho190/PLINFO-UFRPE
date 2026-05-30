from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label
from textual.containers import Center, Vertical, Horizontal

from services.login          import login_service
from utils.password_toggle   import toggle_password


class LoginView(Screen):

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="auth-box"):
                yield Static("🌿 PLINFO", id="title")
                yield Static("Sistema Botânico — UFRPE", classes="subtitle")

                yield Input(placeholder="Digite seu e-mail...", id="email")

                with Horizontal(id="password-row"):
                    yield Input(placeholder="Digite sua senha...", id="password", password=True)
                    yield Button("Mostrar", id="toggle-pw")

                yield Label("", id="message")

                yield Button("Entrar", id="btn-login", variant="primary")
                yield Button("Criar conta", id="btn-register")
                yield Button("Sair", id="btn-exit", variant="error")

    def _validate_email(self) -> None:
        from utils.validations import Validation
        field = self.query_one("#email", Input)
        v = field.value.strip()
        if not v:
            field.remove_class("invalid")
            return
        if Validation.validadion_email(v):
            field.remove_class("invalid")
        else:
            field.add_class("invalid")

    def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "email":
            self._validate_email()
        # Limpa mensagem de erro ao digitar
        self.query_one("#message", Label).update("")

    def on_screen_resume(self) -> None:
        self.query_one("#email",    Input).value = ""
        self.query_one("#password", Input).value = ""
        self.query_one("#email",    Input).remove_class("invalid")
        self.query_one("#message",  Label).update("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        msg = self.query_one("#message", Label)

        if event.button.id == "toggle-pw":
            toggle_password(self, "password", "toggle-pw")
            return

        if event.button.id == "btn-login":
            email    = self.query_one("#email",    Input).value.strip().lower()
            password = self.query_one("#password", Input).value.strip()

            if not email or not password:
                msg.update("Preencha todos os campos.")
                return

            valid, message = login_service.authenticate(email, password)
            if valid:
                from ui.screens.dashboard import DashboardView
                user = login_service.get_user(email)
                msg.update("")
                self.app.push_screen(DashboardView(user))
            else:
                msg.update(message)
            return

        if event.button.id == "btn-register":
            from ui.screens.register import RegisterView
            self.app.push_screen(RegisterView())
            return

        if event.button.id == "btn-exit":
            self.app.exit()
