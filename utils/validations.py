import re 
from utils.utilities import colorir
from colorama import Fore
class Validation:

    @staticmethod
    def validation_name (user_name) -> bool:
        """
        Função que faz a Validação de nome do usuario com biblioteca regex!
        """
        padrao_name = r'^[A-Za-zÀ-ÿ ]{3,}$' #O espaço entre o ultimo colchete e o y , é para ele considerar os espaços entre os nomes
        return re.fullmatch(padrao_name , user_name) is not None

    @staticmethod
    def validadion_email (email):
        """ 
        Função que faz a Validação de E-mail do usuario com regex!
        """
        padrao_email = r'^[a-zA-Z]+[.]+[a-zA-Z]+@ufrpe\.br$'
        return re.fullmatch(padrao_email , email) is not None
    # Aqui o re.match vai comparar o E-mail que o usuario quer cadastrar com o padrao_email , se for Válido retorna True se n retorna False.

    @staticmethod
    def validation_password (password):
        """
        Função que faz a Validação de senha utilizando regex, para definir oq a senha deve conter!
        """
        if len(password) < 8 :
            return False , "⚠️ A senha deve conter no mínimo 08 caracteres"
        if ' ' in password:
            return False , "⚠️ A senha não pode conter espaços"
        if re.search (r'[À-ÿ]' , password):
            return False , "⚠️ A senha não pode conter acentos"
        if not re.search(r'[A-Z]', password):
            return False , "⚠️ A senha deve conter pelo menos uma letra maíuscula"
        if not re.search(r'[0-9]' , password):
            return False , "⚠️ A senha deve ter pelo menos um número" 
        if not re.search(r'[!@#$%^&*(),.?]' , password):
            return False , "⚠️ A senha deve conter ao menos um caractere especial"
        
        return True , (colorir("Senha Validada ✅ " , Fore.GREEN))
    # Nessa função , ele vai válidar se a senha contém os seguintes parâmetros: 08 caract. , 01 Letra maius. , 01 num. , 01 caract. especial !
