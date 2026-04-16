# Aqui irá ficar as funções que irão guardar os menus:
import os
from utils.utils import colorir , invalid_option , option ,clear_screen
from colorama import Fore
import time
from filter import filter_menu
from vitrine import galeria_menu
from config.config_user import config_menu


"""
Menu Inicial!
"""
def initial_menu():
    print(colorir("=" * 45 , Fore.GREEN))
    print(colorir("🍃 Welcome To Plinfo - UFRPE 🍃".center(45) , Fore.GREEN )) # https://emojitool.com/pt , fonte dos emojis (NADA DE GPTECO)
    print(colorir("=" * 45 , Fore.GREEN))
    print()

    print(colorir("[1]" , Fore.CYAN) + " Cadastro ")
    print(colorir("[2]" , Fore.CYAN) + " Login ")
    print(colorir("[0]" , Fore.CYAN) + " Sair ")

    print()
    print(colorir("=" * 45 , Fore.GREEN))

"""
Menu Principal!
"""
def primary_menu(name , email): #Utilizar esses parametros para a parte de config do usuario! 
    while True:  
        
        clear_screen()

        print(colorir("=" * 45 , Fore.GREEN))
        print(colorir(f"🌿 Seja Bem-Vindo: {name} 🌿".center(45) , Fore.GREEN )) 
        print(colorir("=" * 45 , Fore.GREEN))
        print()

        print(colorir("[1]" , Fore.CYAN) + " Mostrar Vitrine ")
        print(colorir("[2]" , Fore.CYAN) + " Filtros ")
        print(colorir("[3]" , Fore.CYAN) + " Config.Usuáro ")
        print(colorir("[0]" , Fore.CYAN) + " Voltar ")

        print()
        print(colorir("=" * 45 , Fore.GREEN))

        user_choice = option()

        if user_choice == 1:
            galeria_menu()
            time.sleep(2)
        elif user_choice == 2:
            filter_menu()
        elif user_choice == 3:
            config_menu(name , email)
        elif user_choice == 0: 
            break
        else:
            invalid_option()