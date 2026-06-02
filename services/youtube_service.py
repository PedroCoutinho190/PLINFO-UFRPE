import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

class YoutubeService:

    def __init__(self):
        self.youtube = build( #Cria uma Conexão com a API do YT
            "youtube",
            "v3",
            developerKey=os.getenv("YOUTUBE_API_KEY")
            )
        
    def buscar_video(self, nome_receita):

        resultado = ( #Tudo que está aqui dentro faz parte da "Convenção da API do YT"
            self.youtube.search()
            .list( #O search é basicamente o user abrir a barra de pesquisa do yt, e o list configura essa pesquisa
                q = f"{nome_receita}, receita", # O "q" que faz a consulta(pesquisa)
                part = "snippet", # Busca Simples (Channel, Descrição, Título...)
                maxResults = 1,
                type = "video",).execute()
        )

        if not resultado["items"]:
            return None
        
        video_id = (
            resultado["items"][0]
            ["id"]["videoId"]
        )

        return(f"https://www.youtube.com/watch?v={video_id}")
    
yt = YoutubeService()