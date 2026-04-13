from utils import colorir , clear_screen
from validations import*
from colorama import Fore
from __menus_interfaces import initial_menu , primary_menu
import time
from __database import insert_database ,search_user

""" 
Função para cadastro do usuario!
"""
def record_newuser():

    while True:

        clear_screen()

        user_name = input(colorir("-> Digite seu Nome: " , Fore.YELLOW)).strip()
        test_name = validation_name(user_name)

        if test_name:
            print(colorir("Ótimo belo nome!", Fore.GREEN))
            time.sleep(2)
            break
        else:
            print(colorir("⚠️ Ops! Acho que você colocou seu nome errado..." , Fore.RED))
            time.sleep(2)

    while True:
        
        clear_screen()

        email = input(colorir("-> Digite seu E-mail (NOME.SOBRENOME@ufrpe.br): " , Fore.YELLOW)).strip().lower()
        result = validadion_email(email)

        if result:
            print(colorir("  E-mail validado ✅" , Fore.GREEN))
            time.sleep(2)
            break
        else:
            print(colorir("E-mail Inválido ❌  , Tente novamente!" , Fore.RED))
            time.sleep(2) #2s de aviso
    
    while True:

        clear_screen()

        print(colorir("Sua senha deve conter ao menos:\n 01 caractere especial \n 01 Letra Maiúscula \n 01 Número \n E no mínimo 8 caracteres " , Fore.WHITE))
        password = input(colorir("-> Digite sua senha: " , Fore.YELLOW)).strip()
        valid , message = validation_password(password) #Aqui o valido entra para receber se é True or False , e o mensagem recebe o tipo de erro la da validation_senha.

        if valid:
            confirmation = input(colorir("-> Confirme sua senha: " , Fore.YELLOW)).strip()   
            if password == confirmation:
                insert_database(user_name , email , password)
                print(colorir("Usuario Cadastrado com sucesso!✅" , Fore.GREEN))
                time.sleep(2) # Pausa antes do menu
                break
            else:
                print(colorir("⚠️ As senhas não correspondem!" , Fore.RED))
                time.sleep(2)
        else:
            print(colorir(message , Fore.RED))
            time.sleep(2)
            continue


"""
Função Login
"""
def login():

    while True:

        clear_screen()

        email = input(colorir("-> Digite seu E-mail: " , Fore.YELLOW)).strip().lower()
        password = input(colorir("-> Digite sua Senha: " , Fore.YELLOW)).strip()

        valid , message = search_user(email , password)

        if valid:
            print(colorir(f"Bem vindo, {message}! ✅" , Fore.GREEN))
            time.sleep(2)
            primary_menu()
            break
        else:
            print(colorir(message , Fore.RED))
            time.sleep(2)
                  