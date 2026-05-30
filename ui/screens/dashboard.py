from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button
from textual.containers import Center, Vertical

from models.user import User


class DashboardView(Screen):
    """Hub principal — escolhe destino após login."""

    def __init__(self, user: User) -> None:
        super().__init__()
        self.current_user = user

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="auth-box"):
                yield Static("🌿 PLINFO 🌿", id="title")
                yield Static(
                    f"Bem-vindo, {self.current_user.user_name}!",
                    classes="subtitle"
                )
                yield Button("Catálogo de Plantas", id="btn-catalog")
                yield Button("Configurações",        id="btn-settings")
                yield Button("Sair",                    id="btn-logout", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-catalog":
            from ui.screens.catalog import CatalogView
            self.app.push_screen(CatalogView())
            return

        if event.button.id == "btn-settings":
            from ui.screens.settings import SettingsView
            self.app.push_screen(SettingsView(self.current_user))
            return

        if event.button.id == "btn-logout":
            self.app.pop_screen()
