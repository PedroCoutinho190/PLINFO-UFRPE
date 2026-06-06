import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class SimulatorService:

    def __init__(self):
        self.groq = Groq()

    def ambient_simulator(self, luminosidade, espaco, clima, umidade):
        try:

            response = self.groq.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=512,
            messages=[
                {
                    "role": "system",
                    "content": """
            Você é um especialista em botânica.

            Sua função é recomendar a planta mais adequada com base nas condições de cultivo fornecidas pelo usuário.

            Retorne SOMENTE um JSON válido, sem markdown e sem qualquer texto adicional.

            Estrutura obrigatória:

            {
                "nome": "",
                "nome_cientifico": "",
                "descricao": "",
                "tipo": "",
                "porte": "",
                "tempo_crescimento": "",
                "dificuldade_cultivo": "",
                "beneficios": [
                    ""
                ],
                "cuidados": [
                    ""
                ],
                "condicoes_ideais": {
                    "luminosidade": "",
                    "clima": "",
                    "umidade": "",
                    "espaco": ""
                }
            }

            Regras:
            - Escolha apenas uma planta.
            - A planta deve ser compatível com as condições recebidas.
            - A descrição deve conter entre 100 e 200 palavras.
            - Os benefícios e cuidados devem conter pelo menos 3 itens cada, priorize detalhes.
            - Não invente espécies inexistentes.
            - Não utilize markdown.
            - Não retorne explicações fora do JSON.
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