from utils import*
"""
Galeria de Plantas!
"""
plantas = [
        # MEDICINAIS
    {"nome": "Babosa", "tipo": "Medicinal", "curiosidades": "Ajuda na pele", "origem": "África", "cuidados": "Regar pouco"},
    {"nome": "Hortelã", "tipo": "Medicinal", "curiosidades": "Ajuda na digestão", "origem": "Europa", "cuidados": "Regar frequentemente"},
    {"nome": "Camomila", "tipo": "Medicinal", "curiosidades": "Calmante natural", "origem": "Ásia", "cuidados": "Sol moderado"},
        # VENENOSAS
    {"nome": "Comigo-ninguém-pode", "tipo": "Venenosa", "curiosidades": "Muito usada para proteção espiritual", "origem": "América do Sul", "cuidados": "Evitar contato"},
    {"nome": "Mamona", "tipo": "Venenosa", "curiosidades": "Produz o óleo de rícino e a ricina", "origem": "África", "cuidados": "Manter longe de crianças"},
    {"nome": "Espada-de-são-jorge", "tipo": "Venenosa", "curiosidades": "Purificadora de Ar", "origem": "África", "cuidados": "Pouca água"},
        # AQUÁTICAS
    {"nome": "Vitória-régia", "tipo": "Aquatica", "curiosidades": "Folhas gigantes", "origem": "Amazônia", "cuidados": "Água constante"},
    {"nome": "Lótus", "tipo": "Aquatica", "curiosidades": "Flor simbólica", "origem": "Ásia", "cuidados": "Água limpa"},
    {"nome": "Alface-d'água", "tipo": "Aquatica", "curiosidades": "Flutua na água", "origem": "América Tropical/América do Sul", "cuidados": "Ambiente úmido"}
    ]
def filter_menu():
    while True:

        clear_screen()

        print("=" * 40)
        print(colorir("🔎 Filtros 🔎".center(40) , Fore.GREEN ))
        print("=" * 40)
        print(colorir("[1]" , Fore.CYAN) + " Plantas Medicinais ")
        print(colorir("[2]" , Fore.CYAN) + " Plantas Venenosas ")
        print(colorir("[3]" , Fore.CYAN) + " Plantas Aquáticas ")
        print(colorir("[4]" , Fore.CYAN) + " Voltar ")
        print("=" * 40)

        opcao = input("Escolha: ")

        # sair
        if opcao == "4":
            print("Encerrando...")
            break

        # escolher tipo
        if opcao == "1":
            tipo = "medicinal"
        elif opcao == "2":
            tipo = "venenosa"
        elif opcao == "3":
            tipo = "aquatica"
        else:
            print("Opção inválida!\n")
            continue

        # filtrar plantas 
        filtradas = [p for p in plantas if p["tipo"].lower() == tipo]
        # mostrar plantas
        clear_screen()
        print("\n=== PLANTAS ===")
        for i, planta in enumerate(filtradas):
            print(f"{i+1} - {planta['nome']}")
        print("4 - Voltar")
        
        try:
            escolha = int(input("Escolha a planta: ")) - 1
            planta = filtradas[escolha]
            if escolha == "4":
                return
        except:
            print("Escolha inválida!\n")
            continue

        # submenu
        clear_screen()
        print(f"\n=== {planta['nome']} ===")
        print("""
    1 - Curiosidades
    2 - Origem
    3 - Cuidados
    4 - Voltar
    """)

        info = input("Escolha: ")

        if info == "4":
            continue
        elif info == "1":
            print("\nCuriosidades:", planta["curiosidades"])
        elif info == "2":
            print("\nOrigem:", planta["origem"])
        elif info == "3":
            print("\nCuidados:", planta["cuidados"])
        else:
            print("Opção inválida!")

        input("\nPressione ENTER para voltar ao menu...")    