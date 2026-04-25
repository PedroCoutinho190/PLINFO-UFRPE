import smtplib
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore
from utils.utilities import colorir

EMAIL_REMETENTE = 'plinfo.ufrpe@gmail.com'
SENHA_APP = 'pjoe skky ouei dcel'

def send_code(email_destino):
    """
    Função que vai realizar o envio do codigo de verificação ao e-mail do usuario logado!
    Recebe como parametro o E-mail DESTINO para envio do cod! 
    """
    codigo = str(random.randint(100000, 999999))

    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = email_destino
        msg['Subject'] = 'Plinfo - Codigo de Verificação'

        corpo = f'Seu codigo de Verificação é: {codigo}\n\nNão compartilhe este codigo com ninguém!'
        msg.attach(MIMEText(corpo, 'plain'))

        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_APP)
        servidor.sendmail(EMAIL_REMETENTE, email_destino, msg.as_string())
        servidor.quit()
        return codigo #Vai retornar o codigo de verificação
    except Exception as e:
        print(colorir(f"Erro ao enviar E-mail: {e}", Fore.RED))
        return None
    
def check_code(email):
    """
    Função para checar se o código que o usuario vai digitar corresponde ao enviado ou não (Máximo 3 tentativas)
    Verifica se o cod foi enviado com sucesso ou não!
    """
    codigo_real = send_code(email)

    if not codigo_real:
        print(colorir('Não foi possivel enviar o codigo', Fore.RED))
        time.sleep(2)
        return False
    print(colorir(f'Codigo enviado para {email}!', Fore.GREEN))

    tentativas = 3
    while tentativas > 0:
        codigo = input(colorir("-> Digite o codigo recebido: ", Fore.YELLOW)).strip()
        if codigo == codigo_real:
            return True 
        tentativas -=1
        if tentativas > 0:
            print(colorir(f"Codigo Incorreto! {tentativas} tentativa(s) restante(s)!", Fore.RED))
            time.sleep(1)

    print(colorir('Tentativas esgotadas!', Fore.RED))
    time.sleep(2)
    return False
