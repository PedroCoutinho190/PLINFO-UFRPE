from database.__database import db
from utils.validations   import Validation
from models.user         import User


class UserConfigService:
    """
    Responsável pelas alterações de dados do usuário logado.
    Sem I/O — só validações e banco de dados.
    A tela (DashboardScreen) cuida de pedir dados e exibir feedback.

    A verificação por e-mail (envio e checagem de código) é feita
    pela DashboardScreen via VerifyCodeModal — não é responsabilidade
    desta classe, pois envolve interação com a interface.
    """

    def __init__(self, db, user: User):
        self.db   = db
        self.user = user

    # ── Nome ──────────────────────────────────────────────
    def update_name(self, new_name: str) -> tuple[bool, str]:
        """
        Valida e salva o novo nome.
        Retorna (True, '') ou (False, mensagem_de_erro).
        """
        if not Validation.validation_name(new_name):
            return False, "Nome inválido — letras e espaços, mín. 3 caracteres."
        self.db.update_name(self.user.email, new_name)
        self.user.user_name = new_name   # atualiza o objeto em memória
        return True, ""

    # ── E-mail ────────────────────────────────────────────
    def validate_email(self, new_email: str) -> tuple[bool, str]:
        """
        Só valida — não salva.
        O save só acontece após a verificação por código (DashboardScreen).
        """
        if not Validation.validadion_email(new_email):
            return False, "E-mail inválido — use: nome.sobrenome@ufrpe.br"
        if self.db.email_exists(new_email):
            return False, "E-mail já cadastrado."
        return True, ""

    def update_email(self, new_email: str) -> None:
        """Salva o novo e-mail após verificação confirmada."""
        self.db.update_email(self.user.email, new_email)
        self.user.email = new_email   # atualiza o objeto em memória

    # ── Senha ─────────────────────────────────────────────
    def validate_password(self, new_password: str, confirm: str) -> tuple[bool, str]:
        """
        Só valida — não salva.
        O save só acontece após a verificação por código (DashboardScreen).
        """
        valid, msg = Validation.validation_password(new_password)
        if not valid:
            return False, msg
        if new_password != confirm:
            return False, "As senhas não correspondem."
        same, _ = self.db.search_user(self.user.email, new_password)
        if same:
            return False, "A nova senha deve ser diferente da atual."
        return True, ""

    def update_password(self, new_password: str) -> None:
        """Salva a nova senha após verificação confirmada."""
        self.db.update_password(self.user.email, new_password)

    # ── Deletar conta ─────────────────────────────────────
    def validate_delete(self, password: str) -> tuple[bool, str]:
        """
        Confirma a senha antes de deletar.
        O delete só acontece após a verificação por código (DashboardScreen).
        """
        valid, _ = self.db.search_user(self.user.email, password)
        if not valid:
            return False, "Senha incorreta."
        return True, ""

    def delete(self) -> None:
        """Deleta a conta após verificação confirmada."""
        self.db.delete_user(self.user.email)
