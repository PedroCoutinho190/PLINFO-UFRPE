from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label, DataTable
from textual.containers import Vertical, Horizontal

from plantas_data.lista_planta import plantas

CATALOG_CSS = """
#topbar {
    height: 3;
    align: left middle;
    background: $panel;
    border-bottom: solid $primary;
    padding: 0 2;
}
#topbar Static { width: 1fr; text-style: bold; }
#filter-row {
    height: 3;
    align: left middle;
    padding: 0 2;
    background: $surface;
    border-bottom: solid $panel;
}
#search {
    width: 1fr;
    margin-right: 2;
    margin-top: 0;
}
.f-btn { margin-top: 0; width: auto; min-width: 14; }
.f-btn.active { color: $primary; text-style: bold; }
#table { height: 1fr; border: none; }
#hint  { height: 1; color: $text-muted; text-align: center; background: $panel; }
"""

class CatalogView(Screen):
    CSS = CATALOG_CSS

    def __init__(self) -> None:
        super().__init__()
        self._search = ""
        self._filter = ""

    def compose(self) -> ComposeResult:
        with Horizontal(id="topbar"):
            yield Button("← Voltar", id="btn-back")
            yield Static("🌿 Catálogo de Plantas")
        with Horizontal(id="filter-row"):
            yield Input(placeholder="Buscar planta...", id="search")
            yield Button("Todas",      id="f-all", classes="f-btn active")
            yield Button("Medicinais", id="f-med", classes="f-btn")
            yield Button("Venenosas",  id="f-ven", classes="f-btn")
            yield Button("Aquáticas",  id="f-aqu", classes="f-btn")
        yield DataTable(id="table", cursor_type="row")
        yield Label("Pressione Enter ou clique para ver detalhes", id="hint")

    def on_mount(self) -> None:
        self._refresh()

    def _refresh(self) -> None:
        t = self.query_one("#table", DataTable)
        t.clear(columns=True)
        t.add_columns("Nome", "Tipo")
        for p in plantas:
            nome, tipo = p.get("nome",""), p.get("tipo","")
            if self._filter and tipo != self._filter: #DUVIDA
                continue
            if self._search and self._search not in nome.lower() and self._search not in tipo.lower():
                continue
            t.add_row(nome, tipo, key=nome)

    def _set_active(self, btn_id: str) -> None:
        for b in ["f-all","f-med","f-ven","f-aqu"]:
            self.query_one(f"#{b}").remove_class("active")
        self.query_one(f"#{btn_id}").add_class("active")

    def on_input_changed(self, event: Input.Changed) -> None:
        self._search = event.value.lower()
        self._refresh()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        bid = event.button.id
        if bid == "btn-back":
            self.app.pop_screen()
        elif bid == "f-all":
            self._filter = ""
            self._search = ""
            self.query_one("#search", Input).value = ""
            self._set_active("f-all")
            self._refresh()
        elif bid == "f-med":
            self._filter = "Medicinal"
            self._set_active("f-med")
            self._refresh()
        elif bid == "f-ven":
            self._filter = "Venenosa"
            self._set_active("f-ven")
            self._refresh()
        elif bid == "f-aqu":
            self._filter = "Aquatica"
            self._set_active("f-aqu")
            self._refresh()

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        from ui.modals.plant_detail import PlantDetailModal
        planta = next((p for p in plantas if p["nome"] == event.row_key.value), None)
        if planta:
            self.app.push_screen(PlantDetailModal(planta))
