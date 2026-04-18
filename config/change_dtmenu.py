from colorama import Fore
from utils.utilities import clear_screen, invalid_option, option, colorir , desenvolvimento
from services.change_name import change_name
"""
Menu de alteração de Dados
"""
def change_dtmenu (email):
    while True:
        clear_screen()
        
        print(colorir("=" * 45, Fore.GREEN))
        print(colorir(" Alterar Dados ".center(45), Fore.GREEN))
        print(colorir("=" * 45, Fore.GREEN))
        print()

        print(colorir(" [1] ", Fore.CYAN) + " Alterar Nome ")
        print(colorir(" [2] ", Fore.CYAN) + " Alterar E-mail ")
        print(colorir(" [3] ", Fore.CYAN) + " Alterar Senha ")
        print(colorir(" [0] ", Fore.CYAN) + " Voltar ")
        print()

        print(colorir("=" * 45, Fore.GREEN))

        user_choice = option()

        if user_choice == 1:
            new_name = change_name(email)
            if new_name:
                return new_name #Isso vai arrumar o "Bug" do nome não ser atualizado na parte do primary menu!
        elif user_choice == 2:
            desenvolvimento()
        elif user_choice == 3:
            desenvolvimento()
        elif user_choice == 0:
            break
        else:
            invalid_option()