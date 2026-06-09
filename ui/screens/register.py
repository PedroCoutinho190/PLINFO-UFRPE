import re
from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label
from textual.containers import Center, Vertical, Horizontal

from services.register     import register as reg_service
from utils.password_toggle import toggle_password


def _clean(t: str) -> str:
    """Remove códigos de escape ANSI/colorama de strings de erro."""
    return re.sub(r"\x1b\[[0-9;]*m", "", str(t))


class RegisterView(Screen):
    """
    Tela de cadastro de novo usuário.

    Coleta nome, e-mail institucional, senha e confirmação de senha.
    Realiza validação em tempo real campo a campo e chama
    RegisterService para persistir o usuário no banco.
    """

    def compose(self) -> ComposeResult:
        """Monta o formulário de cadastro com todos os campos e botões."""
        with Center():
            with Vertical(id="auth-box"):
                yield Static("🌿 PLINFO 🌿", id="title")
                yield Static("Crie sua conta", classes="subtitle")
                yield Input(placeholder="Digite seu nome completo...",        id="name")
                yield Input(placeholder="Digite seu e-mail institucional...", id="email")
                with Horizontal(id="password-row"):
                    yield Input(placeholder="Crie sua senha...",    id="password", password=True)
                    yield Button("Mostrar", id="toggle-pw")
                with Horizontal(id="confirm-row"):
                    yield Input(placeholder="Confirme sua senha...", id="confirm", password=True)
                    yield Button("Mostrar", id="toggle-confirm")
                yield Label("", id="message")
                yield Button("Cadastrar", id="btn-register", variant="primary")
                yield Button("Voltar",    id="btn-back",     variant="primary")

    def _set_invalid(self, field_id: str, invalid: bool) -> None:
        """
        Aplica ou remove a classe CSS 'invalid' em um campo de input.

        Args:
            field_id: ID do widget Input a ser marcado.
            invalid: True para marcar como inválido, False para remover a marcação.
        """
        f = self.query_one(f"#{field_id}", Input)
        f.add_class("invalid") if invalid else f.remove_class("invalid")

    def on_input_changed(self, event: Input.Changed) -> None:
        """
        Valida cada campo em tempo real conforme o usuário digita.

        Regras aplicadas:
        - name: apenas letras e espaços, mínimo 3 caracteres
        - email: padrão nome.sobrenome@ufrpe.br (case insensitive)
        - password: mín. 8 chars, 1 maiúscula, 1 número, 1 especial
        - confirm: deve ser idêntico ao campo password
        """
        from utils.validations import Validation
        fid = event.input.id
        v   = event.value.strip()

        self.query_one("#message", Label).update("")

        if fid == "name" and v:
            self._set_invalid("name", not Validation.validation_name(v))
        elif fid == "email" and v:
            self._set_invalid("email", not Validation.validadion_email(v.lower()))
        elif fid == "password" and v:
            ok, _ = Validation.validation_password(v)
            self._set_invalid("password", not ok)
        elif fid == "confirm" and v:
            pw = self.query_one("#password", Input).value
            self._set_invalid("confirm", v != pw)

        if not v:
            self.query_one(f"#{fid}", Input).remove_class("invalid")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Trata eventos de botão:
        - toggle-pw / toggle-confirm: alterna visibilidade das senhas
        - btn-back: volta para o login
        - btn-register: executa o cadastro
        """
        msg = self.query_one("#message", Label)

        if event.button.id == "toggle-pw":
            toggle_password(self, "password", "toggle-pw")
            return

        if event.button.id == "toggle-confirm":
            toggle_password(self, "confirm", "toggle-confirm")
            return

        if event.button.id == "btn-back":
            self.app.pop_screen()
            return

        if event.button.id == "btn-register":
            self._handle_register(msg)

    def _handle_register(self, msg: Label) -> None:
        """
        Valida todos os campos e chama RegisterService para criar o usuário.

        Exibe mensagem de erro inline em caso de falha em qualquer validação.
        Em caso de sucesso, notifica o usuário e volta para a tela de login.

        Args:
            msg: Label onde mensagens de erro são exibidas.
        """
        name    = self.query_one("#name",     Input).value.strip()
        email   = self.query_one("#email",    Input).value.strip().lower()
        pw      = self.query_one("#password", Input).value.strip()
        confirm = self.query_one("#confirm",  Input).value.strip()

        if not reg_service.validate_name(name):
            msg.update("Nome inválido — use apenas letras, mín. 3 caracteres.")
            self._set_invalid("name", True)
            return

        ok, err = reg_service.validate_email(email)
        if not ok:
            msg.update(err)
            self._set_invalid("email", True)
            return

        ok_pw, err_pw = reg_service.validate_password(pw)
        if not ok_pw:
            msg.update(_clean(err_pw))
            self._set_invalid("password", True)
            return

        if pw != confirm:
            msg.update("As senhas não coincidem.")
            self._set_invalid("confirm", True)
            return

        success, _ = reg_service.register(name, email, pw)
        if success:
            self.app.notify("Conta criada com sucesso! Faça login.", severity="information")
            self.app.pop_screen()
        else:
            msg.update("Erro ao cadastrar. Tente novamente.")
            