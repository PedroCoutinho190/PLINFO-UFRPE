from colorama import Fore
from utils.utilities import clear_screen, invalid_option, option, colorir , desenvolvimento
from config.view_data import view_data
from config.delete_account import delete_account  
"""
Menu da config
"""
def config_menu(name , email):
    while True:

        clear_screen()
        
        print(colorir("=" * 45, Fore.GREEN))
        print(colorir(" Configurações do Usuário".center(45), Fore.GREEN))
        print(colorir("=" * 45, Fore.GREEN))
        print()

        print(colorir(" [1] ", Fore.CYAN) + " Visualizar Dados ")
        print(colorir(" [2] ", Fore.CYAN) + " Alterar senha ")
        print(colorir(" [3] ", Fore.CYAN) + " Deletar Conta ")
        print(colorir(" [0] ", Fore.CYAN) + " Voltar ")
        print()

        print(colorir("=" * 45, Fore.GREEN))

        user_choice = option()

        if user_choice == 1:
            view_data(name , email)
        elif user_choice == 2:
            desenvolvimento()
        elif user_choice == 3:
            delete_account(email)
        elif user_choice == 0:
            break
        else:
            invalid_option()