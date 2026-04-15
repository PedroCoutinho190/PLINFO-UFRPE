from utils import colorir , clear_screen
from validations import*
from colorama import Fore
from __menus_interfaces import initial_menu , primary_menu
import time
from __database import insert_database ,search_user ,email_exists

""" 
Função para cadastro do usuario!
"""
def record_newuser():
    
    cancel = False #Aqui vai ser meu ponto de retorno , caso o usuario tenha um email cadastrado (Vai voltar pro menu e dar a opção de login!)

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
            if email_exists(email):
                print(colorir("⚠️  E-mail já cadastrado! Faça Login." , Fore.YELLOW))
                time.sleep(2)
                cancel = True
                break
            else:
                print(colorir("  E-mail validado ✅" , Fore.GREEN))
                time.sleep(2)
                break
        else:
            print(colorir(" E-mail Inválido ❌  , Tente novamente!" , Fore.RED))
            time.sleep(2) 
    
    if cancel:
        return #Vai retornar para meu ponto de retorno , ou seja , vai encerrar os loops e ir para o menu inicial!

    while True:

        clear_screen()

        print(colorir("Sua senha deve conter ao menos:\n 01 caractere especial \n 01 Letra Maiúscula \n 01 Número \n E no mínimo 8 caracteres " , Fore.WHITE))
        password = input(colorir("-> Digite sua senha: " , Fore.YELLOW)).strip()
        valid , message = validation_password(password) #Aqui o valido entra para receber se é True or False , e o mensagem recebe o tipo de erro la da validation_senha.

        if valid:
            confirmation = input(colorir("-> Confirme sua senha: " , Fore.YELLOW)).strip()   
            if password == confirmation:
                insert_database(user_name , email , password)
                print(colorir("Usuário cadastrado com sucesso! ✅" , Fore.GREEN))
                time.sleep(2)
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
            print(colorir(f"Bem vindo, {message}! ✅" , Fore.GREEN)) #Esse message guarda o user_information [1] = name , do banco de dados !
            time.sleep(2)
            primary_menu(message , email)
            break
        else:
            print(colorir(message , Fore.RED))
            time.sleep(2)
                  