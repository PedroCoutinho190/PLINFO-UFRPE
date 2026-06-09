from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label
from textual.containers import Center, Vertical, Horizontal

from services.login        import login_service
from utils.password_toggle import toggle_password


class LoginView(Screen):
    """
    Tela de autenticação do usuário.

    Responsável por coletar e-mail e senha, validar as credenciais
    via LoginService e empurrar o DashboardView em caso de sucesso.
    """

    def compose(self) -> ComposeResult:
        """Monta a interface de login com campos de e-mail, senha e botões de ação."""
        with Center():
            with Vertical(id="auth-box"):
                yield Static("🌿 PLINFO", id="title")
                yield Static("Sistema Botânico — UFRPE", classes="subtitle")
                yield Input(placeholder="Digite seu e-mail...", id="email")
                with Horizontal(id="password-row"):
                    yield Input(placeholder="Digite sua senha...", id="password", password=True)
                    yield Button("Mostrar", id="toggle-pw")
                yield Label("", id="message")
                yield Button("Entrar",      id="btn-login",    variant="primary")
                yield Button("Criar conta", id="btn-register")
                yield Button("Sair",        id="btn-exit",     variant="error")

    def _validate_email(self) -> None:
        """
        Valida o formato do e-mail em tempo real.

        Aplica a classe CSS 'invalid' no campo caso o e-mail
        não corresponda ao padrão nome.sobrenome@ufrpe.br.
        """
        from utils.validations import Validation
        field = self.query_one("#email", Input)
        value = field.value.strip().lower()
        if not value:
            field.remove_class("invalid")
            return
        if Validation.validadion_email(value):
            field.remove_class("invalid")
        else:
            field.add_class("invalid")

    def on_input_changed(self, event: Input.Changed) -> None:
        """
        Dispara a validação visual do e-mail ao digitar
        e limpa mensagens de erro anteriores.
        """
        if event.input.id == "email":
            self._validate_email()
        self.query_one("#message", Label).update("")

    def on_screen_resume(self) -> None:
        """
        Limpa os campos de e-mail, senha e mensagens de erro
        sempre que a tela volta a ficar ativa (ex: após logout).
        """
        self.query_one("#email",    Input).value = ""
        self.query_one("#password", Input).value = ""
        self.query_one("#email",    Input).remove_class("invalid")
        self.query_one("#message",  Label).update("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Trata os eventos de clique nos botões:
        - toggle-pw: alterna visibilidade da senha
        - btn-login: autentica o usuário
        - btn-register: navega para a tela de cadastro
        - btn-exit: encerra a aplicação
        """
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
            