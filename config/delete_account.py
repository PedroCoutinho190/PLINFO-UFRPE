from utils.utilities import clear_screen , colorir
from colorama import Fore
import time
from database.__database import search_user
from database.__database import delete_user
import maskpass

def delete_account(email):
    """
    Menu de deletamento de conta, caso a conta seja deletada o usuario recebe Logout na hora, e caso ele erre algo, ele sai do menu automaticamente.
    """
    clear_screen()
    
    print(colorir("=" * 45, Fore.GREEN))
    print(colorir("🗑️ Deletar Conta 🗑️".center(45) , Fore.GREEN))
    print(colorir("=" * 45, Fore.GREEN))

    confirmation = input(colorir("-> 🚨 Tem certeza? (s/n): " ,  Fore.YELLOW)).strip().lower()
    if confirmation != 's':
        print(colorir("❌ Operação cancelada." , Fore.YELLOW))
        time.sleep(2)
        return False
    
    senha = maskpass.askpass(colorir("-> Confirme sua senha para deletar: " , Fore.YELLOW) , mask="*").strip()
    valid , _ = search_user(email , senha) #Aqui o message fica guardado , mas não to chamdno ele! poderia usar o _ tbm

    if not valid:
        print(colorir("❌ Senha incorreta! Operação cancelada." , Fore.RED))
        time.sleep(2)
        return False
    
    delete_user(email)
    print(colorir("🚨 Conta deletada com sucesso. Até logo!👋" , Fore.GREEN))
    time.sleep(2)
    return True