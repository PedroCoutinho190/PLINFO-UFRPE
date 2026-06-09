from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label, DataTable
from textual.containers import Vertical, Horizontal

from data.lista_planta import plantas

CATALOG_CSS = """
#topbar {
    height: 5;
    align: left middle;
    background: $panel;
    border-bottom: solid $primary;
    padding: 0 2;
}
#topbar Static { width: 1fr; text-style: bold; }
#filter-row {
    height: 4;
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
    """
    Tela de catálogo de plantas.

    Exibe todas as plantas cadastradas em uma DataTable com suporte a
    busca por nome e filtro por tipo. Cada planta pode ter até 3 tipos,
    exibidos em colunas separadas. Ao selecionar uma linha, abre o
    modal PlantDetailModal com as informações completas da planta.
    """

    CSS = CATALOG_CSS

    def __init__(self) -> None:
        """Inicializa a tela com busca e filtro vazios."""
        super().__init__()
        self._search = ""   # Texto digitado no campo de busca
        self._filter = ""   # Tipo de planta ativo no filtro

    def compose(self) -> ComposeResult:
        """
        Monta a interface com topbar, barra de filtros e tabela de plantas.

        A barra de filtros contém um campo de busca e um botão por tipo de planta.
        """
        with Horizontal(id="topbar"):
            yield Button("← Voltar", id="btn-back")
            yield Static("🌿 Catálogo de Plantas")
        with Horizontal(id="filter-row"):
            yield Input(placeholder="Buscar planta...", id="search")
            yield Button("Todas",       id="f-all", classes="f-btn active")
            yield Button("Medicinais",  id="f-med", classes="f-btn")
            yield Button("Venenosas",   id="f-ven", classes="f-btn")
            yield Button("Aquáticas",   id="f-aqu", classes="f-btn")
            yield Button("Frutíferas",  id="f-fru", classes="f-btn")
            yield Button("Ornamentais", id="f-orn", classes="f-btn")
            yield Button("Aromáticas",  id="f-aro", classes="f-btn")
            yield Button("Nativas",     id="f-nat", classes="f-btn")
            yield Button("Culinárias",  id="f-cul", classes="f-btn")
        yield DataTable(id="table", cursor_type="row")
        yield Label("Pressione Enter ou clique para ver detalhes", id="hint")

    def on_mount(self) -> None:
        """Carrega a tabela ao montar a tela."""
        self._refresh()

    def _refresh(self) -> None:
        """
        Reconstrói a DataTable aplicando o filtro de tipo e a busca ativos.

        Exibe até 3 colunas de tipo por planta. Tipos secundário e terciário
        são exibidos como string vazia quando não existem.
        """
        t = self.query_one("#table", DataTable)
        t.clear(columns=True)
        t.add_columns("Nome", "Tipo Principal", "Tipo Secundário", "Tipo Terciário")
        for p in plantas:
            nome = p.get("nome", "")
            tipo = p.get("tipo", "")
            if self._filter and self._filter not in tipo:
                continue
            if self._search and self._search not in nome.lower() and self._search not in " ".join(tipo).lower():
                continue
            t.add_row(
                nome,
                tipo[0],
                tipo[1] if len(tipo) > 1 else "",
                tipo[2] if len(tipo) > 2 else "",
                key=nome
            )

    def _set_active(self, btn_id: str) -> None:
        """
        Atualiza o destaque visual dos botões de filtro.

        Remove a classe 'active' de todos os botões e a aplica
        apenas no botão correspondente ao filtro selecionado.

        Args:
            btn_id: ID do botão que deve receber a classe 'active'.
        """
        for b in ["f-all","f-med","f-ven","f-aqu","f-fru","f-orn","f-aro","f-nat","f-cul"]:
            self.query_one(f"#{b}").remove_class("active")
        self.query_one(f"#{btn_id}").add_class("active")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Atualiza a busca e recarrega a tabela a cada caractere digitado."""
        self._search = event.value.lower()
        self._refresh()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Trata cliques nos botões de filtro e no botão Voltar.

        Cada botão de filtro define self._filter com o tipo correspondente
        e chama _refresh() para atualizar a tabela.
        """
        bid = event.button.id
        filtros = {
            "f-med": "Medicinal",  "f-ven": "Venenosa",
            "f-aqu": "Aquatica",   "f-fru": "Frutifera",
            "f-orn": "Ornamental", "f-aro": "Aromatica",
            "f-nat": "Nativa",     "f-cul": "Culinaria",
        }
        if bid == "btn-back":
            self.app.pop_screen()
        elif bid == "f-all":
            self._filter = ""
            self._search = ""
            self.query_one("#search", Input).value = ""
            self._set_active("f-all")
            self._refresh()
        elif bid in filtros:
            self._filter = filtros[bid]
            self._set_active(bid)
            self._refresh()

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """
        Abre o modal de detalhes ao selecionar uma linha da tabela.

        Busca a planta pelo nome (row_key) na lista de plantas e
        empurra PlantDetailModal com os dados completos.
        """
        from ui.modals.plant_detail import PlantDetailModal
        planta = next((p for p in plantas if p["nome"] == event.row_key.value), None)
        if planta:
            self.app.push_screen(PlantDetailModal(planta))
            