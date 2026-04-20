from colorama import Fore
from utils.utilities import clear_screen, invalid_option, option, colorir , desenvolvimento
from services.change_name import change_name
from services.change_email import change_email
from services.change_password import change_password
"""
Menu de alteração de Dados
"""
def change_dtmenu (name, email):
    while True:
        clear_screen()
        
        print(colorir("=" * 45, Fore.GREEN))
        print(colorir(" Alterar Dados ".center(45), Fore.GREEN))
        print(colorir("=" * 45, Fore.GREEN))
        print()

        print(colorir(" [1] ", Fore.CYAN) + " Alterar Nome ")
        print(colorir(" [2] ", Fore.CYAN) + " Alterar E-mail ")
        print(colorir(" [3] ", Fore.CYAN) + " Alterar Senha ")
        print(colorir(" [0] ", Fore.CYAN) + " Voltar ↩️")
        print()

        print(colorir("=" * 45, Fore.GREEN))

        user_choice = option()

        if user_choice == 1:
            new_name = change_name(email)
            if new_name:
                name = new_name 
        elif user_choice == 2:
            new_email = change_email(email)
            if new_email:
                email = new_email
        elif user_choice == 3:
            change_password(email)
        elif user_choice == 0:
            return name, email #Vai retornar os 02 valores sempre!
        else:
            invalid_option()