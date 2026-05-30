from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    """
    Class que faz a Representação de um usuário no sistema, o @Dataclass cria o __init__ automaticamente,
    Atributos do User:
    ID: Número de identificação único do usuário, o Optional, serve para caso o usuario ainda não tenha sido criado, podendo ser None ou int.
    name: Nome do usuário
    email: E-mail do usuário
    """
    user_id: Optional[int]
    user_name: str
    email: str  