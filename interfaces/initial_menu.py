# Aqui irá ficar as funções que irão guardar os menus:
import os
from utils.utilities import colorir 
from colorama import Fore

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