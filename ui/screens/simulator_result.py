from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Label, DataTable
from textual.containers import Vertical, Horizontal, ScrollableContainer

RESULT_CSS = """
SimulatorResultView {
    layout: vertical;
    background: $surface;
}
#topbar {
    height: 5;
    align: left middle;
    background: $panel;
    border-bottom: solid $primary;
    padding: 0 2;
}
#topbar Static { width: 1fr; text-style: bold; }
#plant-header {
    height: auto;
    background: $panel;
    padding: 1 2;
    border-bottom: solid $primary;
}
#plant-nome {
    text-style: bold;
    color: $primary;
    content-align: center middle;
    width: 100%;
}
#plant-cientifico {
    color: $text-muted;
    content-align: center middle;
    width: 100%;
}
#info-table {
    height: auto;
    margin: 1 2;
}
#body {
    height: 1fr;
    padding: 0 2;
}
.sec-title {
    text-style: bold;
    color: $primary;
    margin-top: 1;
}
.sec-text { color: $text; height: auto; }
.sec-item { color: $text; height: auto; }
"""


class SimulatorResultView(Screen):
    CSS = RESULT_CSS

    def __init__(self, resultado: dict) -> None:
        super().__init__()
        self.resultado = resultado

    def compose(self) -> ComposeResult:
        r = self.resultado

        with Horizontal(id="topbar"):
            yield Button("← Voltar", id="btn-back")
            yield Static("🌱 Resultado do Simulador")

        with Vertical(id="plant-header"):
            yield Static(r.get("nome", ""), id="plant-nome")
            yield Static(r.get("nome_cientifico", ""), id="plant-cientifico")

        # Tabela com campos rápidos (Nome, científico... e outrs)
        yield DataTable(id="info-table", show_cursor=False)

        # Corpo scrollável com textos longos
        with ScrollableContainer(id="body"):

            if r.get("motivo_escolha"):
                yield Static("Motivo da Escolha", classes="sec-title")
                yield Label(r["motivo_escolha"], classes="sec-text")

            if r.get("descricao"):
                yield Static("Descrição", classes="sec-title")
                yield Label(r["descricao"], classes="sec-text")

            if r.get("beneficios"):
                yield Static("Benefícios", classes="sec-title")
                for b in r["beneficios"]:
                    yield Label(f"• {b}", classes="sec-item")

            if r.get("cuidados"):
                yield Static("Cuidados", classes="sec-title")
                for c in r["cuidados"]:
                    yield Label(f"• {c}", classes="sec-item")

            if r.get("condicoes_ideais"):
                yield Static("Condições Ideais", classes="sec-title")
                ci = r["condicoes_ideais"]
                for k, v in ci.items():
                    yield Label(f"• {k.capitalize()}: {v}", classes="sec-item")

    def on_mount(self) -> None:
        r = self.resultado
        table = self.query_one("#info-table", DataTable)
        table.add_columns("Campo", "Valor")

        campos = [
            ("Tipo",                 r.get("tipo", "")),
            ("Porte",                r.get("porte", "")),
            ("Tempo de Crescimento", r.get("tempo_crescimento", "")),
            ("Dificuldade",          r.get("dificuldade_cultivo", "")),
        ]
        for campo, valor in campos:
            if valor:
                table.add_row(campo, valor)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-back":
            self.app.pop_screen()