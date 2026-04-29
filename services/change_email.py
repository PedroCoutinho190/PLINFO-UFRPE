from utils.utilities import clear_screen , colorir, clear_buffer
from database.__database import update_email , email_exists
from colorama import Fore
from utils.validations import validadion_email
import time
from utils.email_service import check_code


def change_email(email):
    """
    Função para alterar E-mail do usuario,  recebe o parametro email, para identificar o user no banco de dados e alterar o proprio!
    """
    while True:
        clear_screen()
        clear_buffer()

        new_email = input(colorir("Digite seu novo E-mail: " , Fore.YELLOW)).strip().lower()
        valid = validadion_email(new_email)

        if valid:
            if email_exists(new_email):
                print(colorir("E-mail já cadastrado!", Fore.RED))
                time.sleep(2)
                break
            else:
                if not check_code(email): #Toda a Logica de envio, verificação do cod... está aqui! se for valido ele passa, se n ele cancela!
                    return None #Retorna'algo' para atualizar a variavel em memoria do primary_menu (name do user exibido na tela)
                update_email(email, new_email)
                print(colorir("E-mail alterado com sucersso!", Fore.GREEN))
                time.sleep(2)
                return new_email
        else:
            print(colorir(" E-mail inválido!\n Verifique se seu E-mail está no padrão: (NOME.SOBRENOME@UFRPE.BR).", Fore.RED))
            time.sleep(2)
        
