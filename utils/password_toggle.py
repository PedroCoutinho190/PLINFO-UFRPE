"""Utilitário de toggle de senha — padrão do projeto de referência."""
from textual.widgets import Input, Button


def toggle_password(screen, input_id: str, button_id: str) -> None:
    """Alterna visibilidade da senha e texto do botão."""
    field  = screen.query_one(f"#{input_id}",  Input)
    button = screen.query_one(f"#{button_id}", Button)
    field.password = not field.password
    button.label   = "Ocultar" if not field.password else "Mostrar"
