from textual.app        import ComposeResult
from textual.screen     import ModalScreen
from textual.widgets    import Static, Button, Label
from textual.containers import Vertical, ScrollableContainer

DETAIL_CSS = """
PragaDetailModal { align: center middle; }
#pd-card {
    width: 90;
    height: 88%;
    border: round $primary;
    background: $panel;
}
#pd-header {
    background: $surface;
    padding: 1 2;
    border-bottom: solid $primary;
    height: auto;
}
#pd-nome  { content-align: center middle; text-style: bold; color: $primary; }
#pd-desc  { content-align: center middle; color: $text-muted; height: auto; }
#pd-body  { padding: 1 2; height: 1fr; }
.sec-title { text-style: bold; color: $primary; margin-top: 1; }
.sec-item  { color: $text; height: auto; }
#pd-video  { color: $primary; height: auto; margin-top: 1; }
"""


class PragaDetailModal(ModalScreen):
    CSS = DETAIL_CSS

    def __init__(self, praga: dict) -> None:
        super().__init__()
        self.praga = praga

    def compose(self) -> ComposeResult:
        p = self.praga
        with Vertical(id="pd-card"):
            with Vertical(id="pd-header"):
                yield Static(p["nome"], id="pd-nome")
                yield Static(p["descricao"], id="pd-desc")
            with ScrollableContainer(id="pd-body"):
                yield Static("Sintomas", classes="sec-title")
                for s in p.get("sintomas", []):
                    yield Label(f"• {s}", classes="sec-item")

                yield Static("Tratamento", classes="sec-title")
                for t in p.get("tratamento", []):
                    yield Label(f"• {t}", classes="sec-item")

                yield Static("Prevenção", classes="sec-title")
                for v in p.get("prevencao", []):
                    yield Label(f"• {v}", classes="sec-item")

                if p.get("video_url"):
                    yield Static("Vídeo", classes="sec-title")
                    yield Static(p["video_url"], id="pd-video")

            yield Button("← Voltar", id="btn-close", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-close":
            self.dismiss()