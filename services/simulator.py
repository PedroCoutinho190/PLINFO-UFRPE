import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class SimulatorService:
    """
    Responsável por Fazer a sugestão de Plantas ao usuário baseado nas informações do seu ambiente.
    Além de, Retornar várias informações da Planta sugerida, Utiliza a API Do Groq
    """
    def __init__(self):
        self.groq = Groq()

    def ambient_simulator(self, luminosidade, espaco, clima, umidade):
        """
        Método que recebe alguns parâmetros relacionados ao ambiente do usuário e com base nestes, faz a recomendação de Plantas
        para o usuário cultivar em seu ambiente, junto com algumas informações da Planta sugerida. O retorno dessas informações ocorrem 
        no formato JSON.
        """
        try:

            response = self.groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"},
            temperature=0.3, # Reduz a Criatividade e aumenta a consistência estrutural das respostas.
            max_tokens=1000,
            messages=[
                {

                    "role": "system",
                    "content": """
            Você é um especialista em botânica e cultivo de plantas.

            Sua função é analisar as condições de cultivo fornecidas pelo usuário e recomendar a planta mais adequada para aquele ambiente.

            Retorne SOMENTE um JSON válido.

            Estrutura obrigatória:

        {
            "nome": "",
            "nome_cientifico”: "",
            "tipo”: "",
            "porte”: “”,
            "tempo_crescimento": "",
            "dificuldade_cultivo": "",
            "dificuldade": "",
            "descricao": "",
            "motivo_escolha": " ,
            "beneficios": [
            "",
            "",
            ""
            ],
            "cuidados":[
            "",
            "",
            "",
            ],
            "condicoes_ideais": {
            "luminosidade": "",
            "clima": ""
            "umidade": ""
            "espaco": ""
            },
        }

            Regras:

            * Escolha apenas UMA planta.
            * A planta deve ser real e compatível com as condições informadas.
            * Priorize espécies populares e cultivadas no Brasil.
            * Considere luminosidade, clima, umidade e espaço como fatores principais para a escolha.
            * Caso nenhuma planta seja perfeitamente compatível, escolha a mais próxima das condições fornecidas.
            * O campo “motivo_escolha” deve ter no mínimo 20 palavras e no máximo 50 e devec explicar por que a planta foi selecionada (Evite falar o Óbvio).
            * O campo “descricao” deve conter entre 80 e 120 palavras.
            * A descrição deve apresentar características da planta, aparência, origem, necessidades de cultivo, benefícios e curiosidades relevantes.
            * Utilize caracteres de quebra de linha (\n\n) para melhorar a legibilidade.
            * Os benefícios devem conter exatamente 3 itens.
            * Não invente espécies, nomes científicos ou informações botânicas.
            * Preencha todos os campos obrigatoriamente.
            * Retorne apenas o objeto JSON.
            * Certifique-se de fechar corretamente todas as chaves, colchetes e aspas.
            * Não utilize markdown.
            * Não retorne comentários, explicações ou texto fora do JSON.
            * A resposta deve conter apenas um único objeto JSON válido.
            
            """
                },
                {
                    "role": "user",
                    "content": f"""
            Condições de cultivo:

            Luminosidade: {luminosidade}
            Clima: {clima}
            Umidade: {umidade}
            Espaço disponível: {espaco}

            Indique a planta mais adequada.
            """
                }
            ]
            )
            
            texto = response.choices[0].message.content

            return json.loads(texto)

        except json.JSONDecodeError:
            return {"erro": "Resposta Inválida da LLM."}
        except Exception as e:
            return {"erro": f"Erro ao consultar o simulador: {e}"}
        
simulator = SimulatorService()