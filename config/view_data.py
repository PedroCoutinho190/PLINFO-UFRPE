from utils.utilities import*
from colorama import Fore
from database.__database import get_user_data
"""
Vizualização dos Dados dos usuarios!
"""

def view_data(email):
    while True: 
        clear_screen()

        dados = get_user_data(email)
        name = dados[1]
        email_atual = dados[2]
        
        print(colorir("=" * 45, Fore.GREEN))
        print(colorir(" Meus Dados".center(45), Fore.GREEN))
        print(colorir("=" * 45, Fore.GREEN))
        print(colorir("Nome: " , Fore.CYAN) + name)
        print(colorir("E-mail: " , Fore.CYAN) + email_atual)
        print(colorir("[0]" , Fore.CYAN) + " Voltar ")
        print(colorir("=" * 45, Fore.GREEN))

        user_choice = option()

        if user_choice == 0:
            break
        else:
            invalid_option()
            continue
