from utils.utilities import*
from colorama import Fore
"""
Vizualização dos Dados dos usuarios!
"""

def view_data(name , email):
    while True: 
        clear_screen()
        print(colorir("=" * 45, Fore.GREEN))
        print(colorir(" Meus Dados".center(45), Fore.GREEN))
        print(colorir("=" * 45, Fore.GREEN))
        print(colorir("Nome: " , Fore.CYAN) + name)
        print(colorir("E-mail: " , Fore.CYAN) + email)
        print(colorir("[0]" , Fore.CYAN) + " Voltar ")
        print(colorir("=" * 45, Fore.GREEN))

        user_choice = option()

        if user_choice == 0:
            break
        else:
            invalid_option()
            continue
