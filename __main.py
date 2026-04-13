from colorama import init
from function_user import record_newuser , login
from __menus_interfaces import initial_menu 
from utils import clear_screen , invalid_option , option
from __database import creat_database
from utils import colorir
from colorama import Fore

init(autoreset = True)

def main():
    while True:

        clear_screen()
        initial_menu()
        user_choice = option()

        if user_choice == 1:
            record_newuser()
        elif user_choice == 2:
            login()
        elif user_choice == 3:
            print(colorir("Até Breve 👋 ,Encerrando o programa..." , Fore.RED))
            break
        else:
            invalid_option()
            
creat_database()
main()