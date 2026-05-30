from colorama import Style

def colorir (texto , cor):
    """
    Função para colorir palavras/frases, recebe como parametros o texto e cor escolhida
    """
    #Funciona no padrão (colorir("Texto" , Fore.BLACK))
    return cor + texto + Style.RESET_ALL