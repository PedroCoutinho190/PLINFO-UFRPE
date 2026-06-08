import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class RecipeService:
    """
    Responsável por sugerir Nome de Receitas de uma Planta escolhida pelo usuário, além de uma breve descrição sobre a receita.
    """
    def __init__(self):
        self.groq = Groq()

    def buscar_receitas(self, planta: str) -> list | dict:
        """
        Método que Utiliza a API_KEY do Groq para retornar até 05 receitas, recebe planta como parâmetro e caso seja comestível, 
        retorna um JSON contendo (Nome da Receita x Breve Descrição) para facilitar a extração de informações.
        """
        try:
            response = self.groq.chat.completions.create(
                model="llama-3.1-8b-instant",
                max_tokens=600,
                messages=[
                    {
                        "role": "system",
                        "content": """
    Você é um especialista em culinária e plantas alimentícias.

    Retorne APENAS JSON válido.

    Regras obrigatórias:

    - Retorne no máximo 5 receitas.
    - Cada receita deve possuir apenas os campos "nome" e "descricao".
    - Use nomes completos e específicos das receitas.
    - A descrição deve ser breve e objetiva.
    - Não forneça ingredientes.
    - Não forneça modo de preparo.
    - Não forneça links.
    - Não forneça markdown.
    - Não forneça explicações fora do JSON.
    - Não utilize blocos de código.

    Se a planta for tóxica, venenosa ou inadequada para consumo humano, retorne exatamente:

    {"erro":"Esta planta não é adequada para consumo humano."}

    Se a planta não for reconhecida, não existir ou não possuir uso culinário conhecido, retorne exatamente:

    {"erro":"Planta não reconhecida ou sem uso culinário conhecido."}

    Quando a planta for válida, retorne exatamente no formato:

    [
        {
            "nome": "Nome da receita",
            "descricao": "Breve descrição da receita"
        }
    ]

    Exemplo:

    [
        {
            "nome": "Molho Pesto de Manjericão",
            "descricao": "Molho italiano preparado com folhas frescas de manjericão."
        },
        {
            "nome": "Chá de Manjericão",
            "descricao": "Infusão aromática com sabor suave e refrescante."
        }
    ]
    """
                    },
                    {
                        "role": "user",
                        "content": f"Planta: {planta}"
                    }
                ]
            )

            texto = response.choices[0].message.content

            return json.loads(texto)

        except json.JSONDecodeError:
            return {"erro": "Resposta inválida da LLM."}

        except Exception as e:
            return {"erro": f"Erro ao consultar receitas: {e}"}