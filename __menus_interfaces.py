# Aqui irá ficar as funções que irão guardar os menus:
import os
from utils import colorir , invalid_option , option ,clear_screen
from colorama import Fore
import time
from galeria import filter_menu
from vitrine import galeria_menu


"""
Menu Inicial!
"""
def initial_menu():
    print("=" * 40)
    print(colorir("🍃 Welcome To Plinfo - UFRPE 🍃".center(40) , Fore.GREEN )) # https://emojitool.com/pt , fonte dos emojis (NADA DE GPTECO)
    print("=" * 40)
    print(colorir("[1]" , Fore.CYAN) + " Cadastro ")
    print(colorir("[2]" , Fore.CYAN) + " Login ")
    print(colorir("[3]" , Fore.CYAN) + " Sair ")
    print("=" * 40)

"""
Menu Principal!
"""
def primary_menu(name , email): #Utilizar esses parametros para a parte de config do usuario! 
    while True:  
        
        clear_screen()

        print("=" * 40) 
        print(colorir(f"🌿 Seja Bem-Vindo: {name} 🌿".center(40) , Fore.GREEN )) 
        print("=" * 40)
        print(colorir("[1]" , Fore.CYAN) + " Mostrar Vitrine ")
        print(colorir("[2]" , Fore.CYAN) + " Filtros ")
        print(colorir("[3]" , Fore.CYAN) + " Config.Usuáro ")
        print(colorir("[4]" , Fore.CYAN) + " Voltar ")
        print("=" * 40)

        user_choice = option()

        if user_choice == 1:
            galeria_menu()
            time.sleep(2)
        elif user_choice == 2:
            filter_menu()
        elif user_choice == 3:
            print(colorir("Em Desenvolvimento!" , Fore.BLUE))
            time.sleep(2)
        elif user_choice == 4: 
            break
        else:
            invalid_option()

"""
Menu da Vitrine
"""


"""
Menu dos Filtros
"""



"""
Config. Usuário!
"""