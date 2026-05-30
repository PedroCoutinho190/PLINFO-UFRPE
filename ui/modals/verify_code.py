from textual.app        import ComposeResult
from textual.screen     import ModalScreen
from textual.widgets    import Static, Button, Input, Label
from textual.containers import Center, Vertical

VERIFY_CSS = """
VerifyCodeModal {
    align: center middle;
}
#verify-box {
    width: 60;
    height: auto;
    border: round $primary;
    padding: 1 2;
    background: $panel;
}
"""

class VerifyCodeModal(ModalScreen[bool]):
    CSS = VERIFY_CSS

    def __init__(self, email: str, code: str) -> None:
        super().__init__()
        self.target_email = email
        self.real_code    = code
        self.attempts     = 3

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="verify-box"):
                yield Static("🔐 Verificação de E-mail", id="title")
                yield Static(f"Código enviado para: {self.target_email}", classes="subtitle")
                yield Input(placeholder="Digite o código de 6 dígitos...", id="code")
                yield Label("", id="message")
                yield Button("Verificar", id="btn-verify", variant="primary")
                yield Button("Cancelar",  id="btn-cancel")

    def on_mount(self) -> None:
        self.query_one("#code").focus()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.query_one("#message", Label).update("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-cancel":
            self.dismiss(False)
            return

        if event.button.id == "btn-verify":
            typed = self.query_one("#code", Input).value.strip()
            if typed == self.real_code:
                self.dismiss(True)
            else:
                self.attempts -= 1
                if self.attempts > 0:
                    self.query_one("#message", Label).update(
                        f"Código incorreto — {self.attempts} tentativa(s) restante(s)."
                    )
                    self.query_one("#code", Input).value = ""
                else:
                    self.app.notify("Tentativas esgotadas.", severity="error")
                    self.dismiss(False)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.on_button_pressed(type("E", (), {"button": type("B", (), {"id": "btn-verify"})()})())
