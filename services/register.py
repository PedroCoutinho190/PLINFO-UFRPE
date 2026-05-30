from database.__database import db
from utils.validations   import Validation


class RegisterService:
    """
    Responsável pelo cadastro de novos usuários.
    Sem I/O — só validações e banco de dados.
    A tela (RegisterScreen) cuida de pedir e exibir dados.

    Mantém a mesma estrutura de métodos separados por etapa:
    collect_name → collect_email → collect_password
    Agora cada um valida e retorna resultado em vez de usar input/print.
    """

    def __init__(self, db):
        self.db = db

    def validate_name(self, name: str) -> bool:
        """Retorna True se o nome for válido."""
        return Validation.validation_name(name)

    def validate_email(self, email: str) -> tuple[bool, str]:
        """
        Valida formato e verifica se já existe no banco.
        Retorna (True, '') ou (False, mensagem_de_erro).
        """
        if not Validation.validadion_email(email):
            return False, "E-mail inválido — use: nome.sobrenome@ufrpe.br"
        if self.db.email_exists(email):
            return False, "E-mail já cadastrado. Faça login."
        return True, ""

    def validate_password(self, password: str) -> tuple[bool, str]:
        """
        Valida força da senha.
        Retorna (True, msg_sucesso) ou (False, msg_erro).
        """
        return Validation.validation_password(password)

    def register(self, name: str, email: str, password: str) -> tuple[bool, str]:
        """
        Insere o usuário no banco.
        Retorna (True, msg_sucesso) ou (False, msg_erro).
        """
        return self.db.insert_database(name, email, password)


# Objeto global — importado pelas screens
register = RegisterService(db)
