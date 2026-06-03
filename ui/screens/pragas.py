from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label, DataTable
from textual.containers import Vertical, Horizontal

from data.lista_praga import pragas

PRAGAS_CSS = """
PragasView {
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
#search-row {
    height: 4;
    align: left middle;
    padding: 0 2;
    background: $surface;
    border-bottom: solid $panel;
}
#search {
    width: 1fr;
    margin-top: 0;
}
#table { height: 1fr; border: none; }
#hint  { height: 1; color: $text-muted; text-align: center; background: $panel; }
"""


class PragasView(Screen):
    CSS = PRAGAS_CSS

    def __init__(self) -> None:
        super().__init__()
        self._search = ""

    def compose(self) -> ComposeResult:
        with Horizontal(id="topbar"):
            yield Button("← Voltar", id="btn-back")
            yield Static("🐛 Pragas e Doenças")
        with Horizontal(id="search-row"):
            yield Input(placeholder="Buscar praga...", id="search")
        yield DataTable(id="table", cursor_type="row")
        yield Label("Pressione Enter ou clique para ver detalhes", id="hint")

    def on_mount(self) -> None:
        self._refresh()

    def _refresh(self) -> None:
        t = self.query_one("#table", DataTable)
        t.clear(columns=True)
        t.add_columns("Nome", "Descrição")
        for p in pragas:
            nome = p.get("nome", "")
            desc = p.get("descricao", "")
            if self._search and self._search not in nome.lower() and self._search not in desc.lower():
                continue
            t.add_row(nome, desc, key=nome)

    def on_input_changed(self, event: Input.Changed) -> None:
        self._search = event.value.lower()
        self._refresh()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-back":
            self.app.pop_screen()

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        from ui.modals.praga_detail import PragaDetailModal
        praga = next((p for p in pragas if p["nome"] == event.row_key.value), None)
        if praga:
            self.app.push_screen(PragaDetailModal(praga))