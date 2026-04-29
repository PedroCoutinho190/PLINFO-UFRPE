from utils.utilities import clear_screen , colorir, clear_buffer
from colorama import Fore
from database.__database import search_user
import time
from interfaces.primary_menu import primary_menu
import maskpass


def login():
    """
    Função para o Login do usuario, recebe a senha e vai buscar na validação se a senha é valida ou não, se for retorna True = valid 
    Caso não cumpra os parametros, será retornado False e uma message é exibida! (De erro caso o retorno seja Falso e de Acerto caso seja True)
    """

    while True:

        clear_screen()
        clear_buffer()

        email = input(colorir("-> Digite seu E-mail: " , Fore.YELLOW)).strip().lower()
        try:
            password = maskpass.askpass(colorir("-> Digite sua Senha: " , Fore.YELLOW) , mask="*").strip()
        except Exception:
            print(colorir("❌ Erro ao ler a senha, evite caracteres com acentuação(ç, á, à...)", Fore.RED))
            time.sleep(2)   #Isso Vai tratar o erro de UTF-8 que o maskpass n lida bem.
            continue
        valid, message = search_user(email , password)

        if valid:
            print(colorir(f"Bem vindo, {message}! ✅" , Fore.GREEN)) #Esse message guarda o user_information [1] = name , do banco de dados !
            time.sleep(2)
            primary_menu(message , email)
            break
        else:
            print(colorir(message , Fore.RED))
            time.sleep(2)
                  