from utils.utilities import*
from interfaces.filter import filter_menu 
from interfaces.vitrine import galeria_menu
from config.config_user import config_menu


def primary_menu(name , email): #Utilizar esses parametros para a parte de config do usuario!
    """
    Menu Principal! Recebe os parametros email e name que são utilizados para buscar/atualizar possíveis mudanças no banco de dados e exibir o nome atualizado
    no menu.
    """ 
    while True:  
        
        clear_screen()

        print(colorir("=" * 45 , Fore.GREEN))
        print(colorir(f"🌿 Seja Bem-Vindo: {name} 🌿".center(45) , Fore.GREEN )) 
        print(colorir("=" * 45 , Fore.GREEN))
        print()

        print(colorir("[1]" , Fore.CYAN) + " Mostrar Vitrine ")
        print(colorir("[2]" , Fore.CYAN) + " Filtros ")
        print(colorir("[3]" , Fore.CYAN) + " Config.Usuáro ")
        print(colorir("[0]" , Fore.CYAN) + " Voltar ↩️")

        print()
        print(colorir("=" * 45 , Fore.GREEN))

        user_choice = option()

        if user_choice == 1:
            galeria_menu()
            time.sleep(2)
        elif user_choice == 2:
            filter_menu()
        elif user_choice == 3:
            result = config_menu(name , email)
            if result:
                if result == "Logout":
                    break #Sai para o menu inicial / deletou a conta!
                elif result:
                    name, email = result #Atualiza os dados para o menu primario!
        elif user_choice == 0: 
            break
        else:
            invalid_option()