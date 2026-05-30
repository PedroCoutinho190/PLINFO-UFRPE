from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label
from textual.containers import Center, Vertical

from models.user import User
from services.user_config_service import UserConfigService
from database.__database import db


class ChangeNameView(Screen):

    def __init__(self, user: User) -> None:
        super().__init__()
        self.current_user = user
        self.config = UserConfigService(db, user)

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="auth-box"):
                yield Static("Alterar Nome", id="title")
                yield Static(
                    f"Nome atual: {self.current_user.user_name}",
                    classes="subtitle"
                )
                yield Input(placeholder="Novo nome...", id="name")
                yield Label("", id="message")
                yield Button("Salvar", id="btn-save", variant="primary")
                yield Button("Voltar", id="btn-back")

    def on_input_changed(self, event: Input.Changed) -> None:
        from utils.validations import Validation
        v = event.value.strip()
        self.query_one("#message", Label).update("")
        if v:
            f = self.query_one("#name", Input)
            if Validation.validation_name(v):
                f.remove_class("invalid")
            else:
                f.add_class("invalid")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-back":
            self.app.pop_screen()
            return

        if event.button.id == "btn-save":
            name = self.query_one("#name", Input).value.strip()
            ok, msg = self.config.update_name(name)
            if not ok:
                self.query_one("#message", Label).update(msg)
                self.query_one("#name", Input).add_class("invalid")
                return
            self.app.notify("Nome alterado com sucesso!")
            self.app.pop_screen()
