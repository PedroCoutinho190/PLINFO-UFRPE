import asyncio
from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Static, Button, Label, Select, LoadingIndicator
from textual.containers import Vertical, Horizontal
from textual            import work
from services.simulator import simulator

SIMULATOR_CSS = """
SimulatorView {
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
#form {
    height: 1fr;
    padding: 1 2;
}
.sel-label { color: $text-muted; height: 1; margin-top: 1; }
Select { width: 100%; margin-bottom: 0; }
#btn-simular { width: 100%; margin-top: 2; }
#loading { height: 3; display: none; }
#message { height: 2; color: $warning; padding: 0 2; }
"""


class SimulatorView(Screen):
    CSS = SIMULATOR_CSS

    _valores = {"luminosidade": None, "espaco": None, "clima": None, "umidade": None}

    def compose(self) -> ComposeResult:
        with Horizontal(id="topbar"):
            yield Button("← Voltar", id="btn-back")
            yield Static("🌱 Simulador de Ambiente")
        with Vertical(id="form"):
            yield Static("Luminosidade", classes="sel-label")
            yield Select(
                [("Baixa", "Baixa"), ("Moderada", "Moderada"), ("Alta", "Alta")],
                prompt="Selecione...", id="sel-luminosidade"
            )
            yield Static("Espaço disponível", classes="sel-label")
            yield Select(
                [("Pequeno", "Pequeno"), ("Médio", "Médio"), ("Grande", "Grande")],
                prompt="Selecione...", id="sel-espaco"
            )
            yield Static("Clima", classes="sel-label")
            yield Select(
                [("Quente", "Quente"), ("Temperado", "Temperado"), ("Frio", "Frio")],
                prompt="Selecione...", id="sel-clima"
            )
            yield Static("Umidade", classes="sel-label")
            yield Select(
                [("Baixa", "Baixa"), ("Moderada", "Moderada"), ("Alta", "Alta")],
                prompt="Selecione...", id="sel-umidade"
            )
            yield Button("Simular", id="btn-simular", variant="primary")
        yield LoadingIndicator(id="loading")
        yield Label("", id="message")

    def on_select_changed(self, event: Select.Changed) -> None:
        mapa = {
            "sel-luminosidade": "luminosidade",
            "sel-espaco":       "espaco",
            "sel-clima":        "clima",
            "sel-umidade":      "umidade",
        }
        if event.select.id in mapa:
            self._valores[mapa[event.select.id]] = event.value
        self.query_one("#message", Label).update("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-back":
            self.app.pop_screen()
            return

        if event.button.id == "btn-simular":
            if None in self._valores.values():
                self.query_one("#message", Label).update("Preencha todos os campos.")
                return
            self.query_one("#loading").display      = True
            self.query_one("#btn-simular").disabled = True
            self.query_one("#message", Label).update("")
            self._simular()

    @work
    async def _simular(self) -> None:
        loop = asyncio.get_event_loop()
        resultado = await loop.run_in_executor(
            None,
            simulator.ambient_simulator,
            self._valores["luminosidade"],
            self._valores["espaco"],
            self._valores["clima"],
            self._valores["umidade"],
        )

        self.query_one("#loading").display      = False
        self.query_one("#btn-simular").disabled = False

        if "erro" in resultado:
            self.query_one("#message", Label).update(resultado["erro"])
            return

        # Empurra a tela de resultado com os dados
        from ui.screens.simulator_result import SimulatorResultView
        self.app.push_screen(SimulatorResultView(resultado))