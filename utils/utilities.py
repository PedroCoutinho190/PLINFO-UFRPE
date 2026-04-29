import os
from colorama import Back , Fore , Style 
import time
import msvcrt
def clear_screen ():
    """
    Função para limpar a tela
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def colorir (texto , cor):
    """
    Função para colorir palavras/frases, recebe como parametros o texto e cor escolhida
    """
    #Funciona no padrão (colorir("Texto" , Fore.BLACK))
    return cor + texto + Style.RESET_ALL


def option ():
    """
    Função que da uma Opção ao usuario e ja trata erros, usada nos menus de navegação do projeto!
    """
    clear_buffer()
    try:
        return int(input(colorir("-> Digite uma opção: " , Fore.YELLOW)))
    except:
        return "a" # Vai jogar o usuario na invalid_option()


def invalid_option ():
    """
    Função Opção Inválida, usada para tratamento de erros do usuario!
    """
    print(colorir("-> Opção Inválida! ❌" , Fore.RED))
    time.sleep(2)
    input(colorir("Digite uma tecla para continuar... " , Fore.LIGHTWHITE_EX))


def desenvolvimento():
    """
    Função que retorna o "em desenvolvimento", utilizada durante o projeto para não deixar vazio/ sem resposta (Abas em construção)
    """
    print(colorir("Em desenvolvimento..." , Fore.BLUE))
    time.sleep(2)


def clear_buffer():
    """
    Essa Função evita que teclas que foram pressionadas anteriormente sejam processadas, ela limpa o Buffer do Teclado, previnindo problemas
    """
    while msvcrt.kbhit():
        msvcrt.getch()


