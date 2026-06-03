import asyncio
from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Input, Label, LoadingIndicator
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual            import work

from services.recipe_service  import RecipeService
from services.youtube_service import yt

RECIPES_CSS = """
RecipesView {
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
#plant-input {
    width: 1fr;
    margin-top: 0;
    margin-right: 2;
}
#btn-search {
    width: auto;
    min-width: 20;
    margin-top: 0;
}
#loading {
    height: 3;
    display: none;
}
#message {
    height: 2;
    color: $warning;
    padding: 0 2;
}
#results {
    height: 1fr;
    padding: 1 2;
}
.recipe-card {
    background: $panel;
    padding: 1 2;
    margin-bottom: 1;
    height: auto;
}
.recipe-nome {
    text-style: bold;
    color: $primary;
}
.recipe-desc {
    color: $text-muted;
    height: auto;
}
.recipe-link {
    color: $primary;
    height: auto;
    margin-top: 1;
}
#hint {
    height: 1;
    color: $text-muted;
    text-align: center;
    background: $panel;
}
"""


class RecipesView(Screen):
    CSS = RECIPES_CSS

    def __init__(self) -> None:
        super().__init__()
        self._recipe_service = RecipeService()

    def compose(self) -> ComposeResult:
        with Horizontal(id="topbar"):
            yield Button("← Voltar", id="btn-back")
            yield Static("🍃 Receitas com Plantas")
        with Horizontal(id="search-row"):
            yield Input(
                placeholder="Digite o nome de uma planta...",
                id="plant-input"
            )
            yield Button("Buscar Receitas", id="btn-search", variant="primary")
        yield LoadingIndicator(id="loading")
        yield Label("", id="message")
        yield ScrollableContainer(id="results")
        yield Label("Os resultados combinam sugestões da IA com vídeos do YouTube", id="hint")

    def on_mount(self) -> None:
        self.query_one("#plant-input").focus()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.query_one("#message", Label).update("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-back":
            self.app.pop_screen()
            return

        if event.button.id == "btn-search":
            planta = self.query_one("#plant-input", Input).value.strip()
            if not planta:
                self.query_one("#message", Label).update("Digite o nome de uma planta.")
                return
            self._iniciar_busca(planta)

    def _iniciar_busca(self, planta: str) -> None:
        # Limpa resultados anteriores
        results = self.query_one("#results", ScrollableContainer)
        results.remove_children()

        self.query_one("#loading").display    = True
        self.query_one("#btn-search").disabled = True
        self.query_one("#message", Label).update("")

        self._buscar(planta)

    @work
    async def _buscar(self, planta: str) -> None:
        loop = asyncio.get_event_loop()

        # 1 — Groq: busca receitas
        receitas = await loop.run_in_executor(
            None, self._recipe_service.buscar_receitas, planta
        )

        self.query_one("#loading").display     = False
        self.query_one("#btn-search").disabled = False

        # Verifica erro retornado pelo Groq
        if isinstance(receitas, dict) and "erro" in receitas:
            self.query_one("#message", Label).update(receitas["erro"])
            return

        results = self.query_one("#results", ScrollableContainer)

        # 2 — Para cada receita, busca vídeo no YouTube
        for receita in receitas:
            nome  = receita.get("nome", "")
            desc  = receita.get("descricao", "")

            video_url = await loop.run_in_executor(
                None, yt.buscar_video, nome
            )

            # Monta o card da receita
            card = Vertical(classes="recipe-card")
            await results.mount(card)
            await card.mount(Static(nome, classes="recipe-nome"))
            await card.mount(Static(desc, classes="recipe-desc"))

            link_texto = video_url if video_url else "Vídeo não encontrado."
            await card.mount(Static(f"▶ {link_texto}", classes="recipe-link"))