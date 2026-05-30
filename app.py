from textual.app import App
from database.__database import db
from ui.screens.login import LoginView
from textual.theme import Theme

PLINFO_THEME = Theme(
    name="plinfo",
    primary="#3fb950",
    error="#f85149",
    warning="#d29922",
    success="#3fb950",
)

# CSS global — sobrescreve as variáveis de tema do Textual

PLINFO_CSS = """
Screen {
    background: $surface;
    align: center middle;
}

#auth-box {
    width: 58;
    height: auto;
    border: round $primary;
    padding: 1 2;
    background: $panel;
}

#title {
    content-align: center middle;
    text-style: bold;
    margin-bottom: 1;
}

.subtitle {
    content-align: center middle;
    color: $text-muted;
    margin-bottom: 1;
}

Input {
    width: 100%;
    margin-top: 1;
}

Input.invalid {
    border: tall $error;
}

Button {
    width: 100%;
    margin-top: 1;
}

#message {
    width: 100%;
    height: 2;
    margin-top: 1;
    color: $warning;
}

#password-row, #confirm-row {
    width: 100%;
    height: auto;
    margin-top: 1;
}

#password-row Input, #confirm-row Input {
    width: 1fr;
    margin-top: 0;
}

#toggle-pw, #toggle-confirm {
    width: 12;
    min-width: 12;
    margin-top: 0;
    margin-left: 1;
}

#password-row Button, #confirm-row Button {
    margin-top: 0;
}
"""


class PlinfApp(App):
    TITLE = "PLINFO — Sistema Botânico UFRPE"
    CSS   = PLINFO_CSS

    def on_mount(self) -> None:
        self.register_theme(PLINFO_THEME)
        self.theme = "plinfo"
        db.creat_database()
        self.push_screen(LoginView())
