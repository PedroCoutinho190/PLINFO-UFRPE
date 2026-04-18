from utils.utilities import clear_screen , colorir
from database.__database import update_email , email_exists
from colorama import Fore
from utils.validations import validadion_email
import time

"""
Função para alterar E-mail do usuario
"""

def change_email(email):
    while True:
        clear_screen()

        new_email = input(colorir("Digite seu novo E-mail: " , Fore.YELLOW)).strip().lower()
        valid = validadion_email(new_email)

        if valid:
            if email_exists(new_email):
                print(colorir("E-mail já cadastrado!", Fore.RED))
                time.sleep(2)
                continue
            else:
                update_email(email, new_email)
                print(colorir("E-mail alterado com sucersso!", Fore.GREEN))
                time.sleep(2)
                return new_email
        else:
            print(colorir(" E-mail inválido!\n Verifique se seu E-mail está no padrão: (NOME.SOBRENOME@UFRPE.BR).", Fore.RED))
            time.sleep(2)
        
