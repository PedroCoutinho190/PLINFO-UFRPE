from utils.utilities import clear_screen, colorir
from database.__database import update_password, search_user
from colorama import Fore
from utils.validations import validation_password
import time

"""
Função para troca de senha!
"""

def change_password(email):
    while True:
        clear_screen()

        new_password = input(colorir("Digite sua nova Senha: ", Fore.YELLOW)).strip()
        valid, message = validation_password(new_password)

        if not valid:
            print(colorir(message, Fore.RED))
            time.sleep(2)
        else:
            senha_existe, _ = search_user(email, new_password)
            if senha_existe:
                print(colorir("A nova senha deve ser diferente da atual!", Fore.RED))
                time.sleep(2)
            else:
                update_password(email, new_password)
                print(colorir("Senha alterada com sucesso!", Fore.GREEN))
                time.sleep(2)
                break