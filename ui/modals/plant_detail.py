from textual.app        import ComposeResult
from textual.screen     import ModalScreen
from textual.widgets    import Static, Button, Label
from textual.containers import Center, Vertical, ScrollableContainer

DETAIL_CSS = """
PlantDetailModal { align: center middle; }
#detail-box {
    width: 90;
    height: 85%;
    border: round $primary;
    background: $panel;
}
#detail-header {
    background: $surface;
    padding: 1 2;
    border-bottom: solid $primary;
    height: auto;
}
#plant-nome  { content-align: center middle; text-style: bold; color: $primary; }
#plant-tipo  { content-align: center middle; color: $text-muted; }
#detail-body { padding: 1 2; height: 1fr; }
.sec-title   { text-style: bold; color: $primary; margin-top: 1; }
.sec-body    { color: $text; height: auto; margin-bottom: 1; }
"""

class PlantDetailModal(ModalScreen):
    CSS = DETAIL_CSS

    _SECTIONS = [
        ("curiosidades",    "Curiosidades"),
        ("origem",          "Origem"),
        ("cuidados",        "Cuidados"),
        ("reflorestamento", "Reflorestamento"),
        ("cultivo",         "Cultivo"),
        ("linha_do_tempo",  "Linha do Tempo")
    ]

    def __init__(self, planta: dict) -> None:
        super().__init__()
        self.planta = planta

    def compose(self) -> ComposeResult:
        p = self.planta
        with Vertical(id="detail-box"):
            with Vertical(id="detail-header"):
                yield Static(p["nome"], id="plant-nome")
                yield Static(", ".join(p["tipo"]), id="plant-tipo") #Transformando o Tipo da planta de lista para str com o join, exibir para o modal quando clicar na planta!(Descrição melhor)
            with ScrollableContainer(id="detail-body"):
                for key, label in self._SECTIONS:
                    if key in p:
                        yield Static(label, classes="sec-title")
                        yield Label(p[key], classes="sec-body")
            yield Button("← Voltar", id="btn-close", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-close":
            self.dismiss()
            