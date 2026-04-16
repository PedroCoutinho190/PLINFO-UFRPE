from colorama import init
from services.register import record_newuser 
from services.login import login
from interfaces.initial_menu import initial_menu 
from utils.utilities import clear_screen , invalid_option , option , colorir
from database.__database import creat_database
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
        elif user_choice == 0:
            print(colorir("Até Breve 👋 ,Encerrando o programa..." , Fore.RED))
            break
        else:
            invalid_option()
            
creat_database()
main()