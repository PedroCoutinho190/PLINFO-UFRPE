# Aqui irá ficar as funções que irão guardar os menus:
import os
from utils import colorir , invalid_option , option ,clear_screen
from colorama import Fore
import time

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
def primary_menu():
    while True:  
        
        clear_screen()

        print("=" * 40) 
        print(colorir("🌿 Menu Principal 🌿".center(40) , Fore.GREEN )) 
        print("=" * 40)
        print(colorir("[1]" , Fore.CYAN) + " Mostrar Vitrine ")
        print(colorir("[2]" , Fore.CYAN) + " Filtros ")
        print(colorir("[3]" , Fore.CYAN) + " Config.Usuáro ")
        print(colorir("[4]" , Fore.CYAN) + " Voltar ")
        print("=" * 40)

        user_choice = option()

        if user_choice == 1:
            print(colorir("Em Desenvolvimento" , Fore.BLUE))
            time.sleep(2)
        elif user_choice == 2:
            filter_menu()
            time.sleep(2)
        elif user_choice == 3:
            print(colorir("Em Desenvolvimento!" , Fore.BLUE))
            time.sleep(2)
        elif user_choice == 4: # O Break aqui vai puxar pra o Menu inicial (Vai fazer a função de voltar!)
            break
        else:
            invalid_option()

"""
Menu da Vitrine
"""


"""
Menu dos Filtros
"""
def filter_menu():
    
    while True:

        clear_screen()

        print("=" * 40)
        print(colorir("🔎 Filtros 🔎".center(40) , Fore.GREEN ))
        print("=" * 40)
        print(colorir("[1]" , Fore.CYAN) + " Plantas Medicinais ")
        print(colorir("[2]" , Fore.CYAN) + " Plantas Venenosas ")
        print(colorir("[3]" , Fore.CYAN) + " Plantas Aquáticas ")
        print(colorir("[4]" , Fore.CYAN) + " Voltar ")
        print("=" * 40)

        user_choice = option()

        if user_choice == 1:
            print("...")
        elif user_choice == 2:
            print("...")
        elif user_choice == 3:
            print("...")
        elif user_choice == 4:
            break
        else:
            invalid_option()