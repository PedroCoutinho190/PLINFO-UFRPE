from utils.utilities import clear_screen , colorir, clear_buffer
from database.__database import update_name
from colorama import Fore
from utils.validations import validation_name
import time



def change_name(email):
    """
    Função para alterar nome do usuario, recebe o parametro email, para identificar o user no banco de dados!
    """
    while True:
        clear_screen()
        clear_buffer()

        new_name = input(colorir("-> Digite o novo nome: " , Fore.YELLOW)).strip()
        valid = validation_name(new_name)

        if valid:
            update_name(email, new_name)
            print(colorir("Nome alterado com sucesso!", Fore.GREEN))
            time.sleep(2)
            return new_name
        else:
            print(colorir("Tente inserir um nome válido", Fore.RED))
            time.sleep(2)
            continue

