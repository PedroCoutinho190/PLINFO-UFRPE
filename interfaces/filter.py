from utils.utilities import *

"""
Galeria de Plantas!
"""
plantas = [
    # MEDICINAIS
    {
        "nome": "Babosa",
        "tipo": "Medicinal",
        "curiosidades": """A babosa (Aloe vera) é uma planta suculenta, perene, pertencente à família Asphodelaceae. Apresenta folhas espessas, carnosas e dispostas em roseta, com bordas serrilhadas. Essas folhas armazenam água, caracterizando sua adaptação a ambientes áridos.

O interior das folhas contém um gel rico em compostos bioativos, como polissacarídeos, vitaminas e enzimas, amplamente estudados por suas propriedades medicinais e cicatrizantes.""",
        "origem": """A espécie é originária de regiões de clima seco, especialmente do norte da África e da região do Mediterrâneo. Atualmente, encontra-se amplamente distribuída em áreas tropicais e subtropicais ao redor do mundo, incluindo o Brasil.""",
        "cuidados": """A babosa apresenta baixa exigência de manutenção, mas requer condições específicas para bom desenvolvimento:

- Necessita de alta luminosidade ou sol pleno
- Deve ser cultivada em solo bem drenado, preferencialmente arenoso
- A irrigação deve ser moderada, evitando encharcamento
- É sensível a baixas temperaturas e geadas

O excesso de água é o principal fator de risco, podendo causar apodrecimento das raízes."""
    },

    {
        "nome": "Hortelã",
        "tipo": "Medicinal",
        "curiosidades": """A hortelã é uma planta aromática muito utilizada na culinária e na medicina natural. Possui propriedades digestivas, refrescantes e pode ajudar no alívio de dores de cabeça e congestão nasal.""",
        "origem": """Originária da Europa e Ásia, a hortelã se adaptou facilmente a diferentes regiões do mundo, sendo hoje amplamente cultivada em climas temperados e tropicais.""",
        "cuidados": """A hortelã cresce com facilidade, mas requer alguns cuidados:

- Prefere locais com meia sombra
- Solo deve ser úmido e rico em matéria orgânica
- Regas frequentes, sem deixar o solo seco
- Pode se espalhar rapidamente, então é ideal controlar seu crescimento"""
    },

    {
        "nome": "Camomila",
        "tipo": "Medicinal",
        "curiosidades": """A camomila é famosa por seu efeito calmante, sendo amplamente utilizada em chás para reduzir ansiedade e melhorar o sono. Também possui propriedades anti-inflamatórias.""",
        "origem": """Originária da Europa e da Ásia Ocidental, a camomila se espalhou por diversas partes do mundo devido ao seu uso medicinal.""",
        "cuidados": """Para um bom cultivo:

- Necessita de sol moderado
- Solo leve e bem drenado
- Regas regulares, evitando excesso de água
- Prefere climas amenos"""
    },

    # VENENOSAS
    {
        "nome": "Comigo-ninguém-pode",
        "tipo": "Venenosa",
        "curiosidades": """Muito popular no Brasil, essa planta é associada à proteção espiritual. No entanto, é altamente tóxica se ingerida, podendo causar irritações severas.""",
        "origem": """Originária da América do Sul, especialmente de regiões tropicais.""",
        "cuidados": """Apesar de resistente:

- Manter fora do alcance de crianças e animais
- Evitar contato com a seiva
- Prefere ambientes internos com luz indireta
- Regas moderadas"""
    },

    {
        "nome": "Mamona",
        "tipo": "Venenosa",
        "curiosidades": """A mamona produz o óleo de rícino, amplamente utilizado industrialmente, mas suas sementes contêm ricina, uma substância altamente tóxica.""",
        "origem": """Originária da África, hoje é cultivada em várias regiões tropicais.""",
        "cuidados": """Cuidados importantes:

- Evitar contato direto com sementes
- Manter longe de crianças
- Prefere sol pleno
- Solo bem drenado"""
    },

    {
        "nome": "Espada-de-são-jorge",
        "tipo": "Venenosa",
        "curiosidades": """Muito usada como planta ornamental, é conhecida por purificar o ar e por seu simbolismo de proteção espiritual.""",
        "origem": """Originária da África Ocidental.""",
        "cuidados": """Fácil de cuidar:

- Pouca rega
- Resistente a ambientes internos
- Prefere luz indireta ou meia sombra
- Evitar excesso de água"""
    },

    # AQUÁTICAS
    {
        "nome": "Vitória-régia",
        "tipo": "Aquatica",
        "curiosidades": """Conhecida por suas folhas gigantes que podem suportar peso, é uma das plantas mais icônicas da Amazônia.""",
        "origem": """Originária da região amazônica.""",
        "cuidados": """Necessita de condições específicas:

- Água abundante e limpa
- Exposição ao sol
- Ambiente quente e úmido
- Espaço amplo para crescimento"""
    },

    {
        "nome": "Lótus",
        "tipo": "Aquatica",
        "curiosidades": """Símbolo de pureza e espiritualidade em várias culturas asiáticas, especialmente no budismo.""",
        "origem": """Originária da Ásia.""",
        "cuidados": """Para cultivo:

- Água limpa e parada
- Bastante luz solar
- Solo lodoso
- Temperatura estável"""
    },

    {
        "nome": "Alface-d'água",
        "tipo": "Aquatica",
        "curiosidades": """Planta flutuante que ajuda na filtragem da água e no equilíbrio de ecossistemas aquáticos.""",
        "origem": """Regiões tropicais das Américas.""",
        "cuidados": """Cuidados básicos:

- Água limpa
- Ambiente úmido
- Boa iluminação
- Controle de crescimento, pois se espalha rapidamente"""
    }
]



def filter_menu():
    while True:

        clear_screen()

        print(colorir("=" * 45, Fore.GREEN))
        print(colorir("🔎 FILTROS 🔎".center(45), Fore.GREEN))
        print(colorir("=" * 45, Fore.GREEN))
        print()

        print(colorir(" [1] ", Fore.CYAN) + "🌱 Plantas Medicinais")
        print(colorir(" [2] ", Fore.CYAN) + "☠️  Plantas Venenosas")
        print(colorir(" [3] ", Fore.CYAN) + "💧 Plantas Aquáticas")
        print(colorir(" [0] ", Fore.CYAN) + "↩️  Voltar")

        print()
        print(colorir("=" * 45, Fore.GREEN))

        entrada = input(colorir("-> Digite uma opção: " , Fore.YELLOW)).strip()

        if not entrada.isdigit():
            print(colorir("Digite apenas números!", Fore.RED))
            input("Pressione ENTER...")
            continue

        opcao = int(entrada)

        if opcao == 0:
            break
        elif opcao == 1:
            tipo = "medicinal"
        elif opcao == 2:
            tipo = "venenosa"
        elif opcao == 3:
            tipo = "aquatica"
        else:
            print(colorir("Opção inválida! ❌", Fore.RED))
            input("Pressione ENTER...")
            continue

        filtradas = [p for p in plantas if p["tipo"].lower() == tipo]

        # =========================
        # LISTA FILTRADA
        # =========================
        while True:

            clear_screen()

            print(colorir("=" * 45, Fore.GREEN))
            print(colorir(f"🌿 {tipo.upper()} 🌿".center(45), Fore.GREEN))
            print(colorir("=" * 45, Fore.GREEN))
            print()

            for i, planta in enumerate(filtradas):
                print(colorir(f" [{i+1}] ", Fore.CYAN) + f"{planta['nome']}")

            print(colorir(" [0] ", Fore.CYAN) + "↩️  Voltar")

            print()
            print(colorir("=" * 45, Fore.GREEN))

            entrada = input("Escolha a planta: ").strip()

            if not entrada.isdigit():
                print(colorir("Digite apenas números!", Fore.RED))
                input("Pressione ENTER...")
                continue

            escolha = int(entrada)

            if escolha == 0:
                break

            if escolha < 1 or escolha > len(filtradas):
                print(colorir("Número fora da lista!", Fore.RED))
                input("Pressione ENTER...")
                continue

            planta = filtradas[escolha - 1]

            # =========================
            # SUBMENU
            # =========================
            while True:

                clear_screen()

                print(colorir("=" * 45, Fore.GREEN))
                print(colorir(f"🌱 {planta['nome']} 🌱".center(45), Fore.GREEN))
                print(colorir("=" * 45, Fore.GREEN))
                print()

                print(colorir(" [1] ", Fore.CYAN) + "📌 Curiosidades")
                print(colorir(" [2] ", Fore.CYAN) + "🌍 Origem")
                print(colorir(" [3] ", Fore.CYAN) + "💧 Cuidados")
                print(colorir(" [0] ", Fore.CYAN) + "↩️  Voltar")

                print()
                print(colorir("=" * 45, Fore.GREEN))

                entrada = input("-> Digite uma opção: ").strip()

                if not entrada.isdigit():
                    print(colorir("Digite apenas números!", Fore.RED))
                    input("Pressione ENTER...")
                    continue

                info = int(entrada)

                if info == 0:
                    break
                elif info == 1:
                    print("\n📌 Curiosidades:", planta["curiosidades"])
                elif info == 2:
                    print("\n🌍 Origem:", planta["origem"])
                elif info == 3:
                    print("\n💧 Cuidados:", planta["cuidados"])
                else:
                    print(colorir("Opção inválida! ❌", Fore.RED))

                input("\nPressione ENTER para continuar...")