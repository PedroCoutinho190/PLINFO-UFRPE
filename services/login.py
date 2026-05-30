from database.__database import db
from models.user         import User


class LoginService:
    """
    Responsável pela autenticação do usuário.
    Sem I/O — só lógica e banco de dados.
    A tela (LoginScreen) cuida de pedir e exibir dados.
    """

    def __init__(self, db):
        self.db = db

    def authenticate(self, email: str, password: str) -> tuple[bool, str]:
        """
        Valida as credenciais no banco.
        Retorna (True, nome_do_usuario) ou (False, mensagem_de_erro).
        """
        return self.db.search_user(email, password)

    def get_user(self, email: str) -> User:
        """
        Busca os dados completos do usuário e retorna um objeto User.
        Só chame após authenticate() retornar True.
        """
        data = self.db.get_user_data(email)
        return User(data[0], data[1], data[2])


# Objeto global — importado pelas screens
login_service = LoginService(db)
