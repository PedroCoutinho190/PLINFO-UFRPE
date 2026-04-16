import os
from colorama import Back , Fore , Style 
import time
"""
Função para limpar a tela
"""
def clear_screen ():
    os.system('cls' if os.name == 'nt' else 'clear')

"""
Função para colorir str
"""
#Funciona no padrão (colorir("Texto" , Fore.BLACK))

def colorir (texto , cor):
    return cor + texto + Style.RESET_ALL

"""
Função Opção
"""
def option ():
    try:
        return int(input(colorir("-> Digite uma opção: " , Fore.YELLOW)))
    except:
        return 0 # Vai jogar o usuario na invalid_option()
"""
Função Opção Inválida
"""
def invalid_option ():
    print(colorir("-> Opção Inválida! ❌" , Fore.RED))
    time.sleep(2)
    input(colorir("Digite uma tecla para continuar... " , Fore.LIGHTWHITE_EX))


"""
Em desenvolvimento
"""
def desenvolvimento():
    print(colorir("Em desenvolvimento..." , Fore.BLUE))
    time.sleep(2)