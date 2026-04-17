from utils.utilities import *

"""
Galeria de Plantas!
"""
plantas = [
    # MEDICINAIS
    {
        "nome": "Babosa",
        "tipo": "Medicinal",
        "curiosidades": "Muito usada em cosméticos, ajuda na cicatrização e hidratação da pele.",
        "origem": "África",
        "cuidados": "Regar pouco, solo bem drenado e bastante luz solar. Evitar excesso de água."
    },
    {
        "nome": "Hortelã",
        "tipo": "Medicinal",
        "curiosidades": "Usada em chás e remédios naturais, ajuda na digestão e refresca o hálito.",
        "origem": "Europa",
        "cuidados": "Regar frequentemente, manter em local com meia sombra e solo úmido."
    },
    {
        "nome": "Camomila",
        "tipo": "Medicinal",
        "curiosidades": "Muito conhecida por seu efeito calmante e ajuda no sono.",
        "origem": "Ásia",
        "cuidados": "Precisa de sol moderado e solo bem drenado. Regar regularmente sem encharcar."
    },

    # VENENOSAS
    {
        "nome": "Comigo-ninguém-pode",
        "tipo": "Venenosa",
        "curiosidades": "Popular em casas brasileiras, associada à proteção espiritual.",
        "origem": "América do Sul",
        "cuidados": "Evitar contato direto, manter fora do alcance de crianças e animais."
    },
    {
        "nome": "Mamona",
        "tipo": "Venenosa",
        "curiosidades": "Produz o óleo de rícino, mas suas sementes são altamente tóxicas.",
        "origem": "África",
        "cuidados": "Manter longe de crianças, usar luvas ao manusear."
    },
    {
        "nome": "Espada-de-são-jorge",
        "tipo": "Venenosa",
        "curiosidades": "Conhecida por purificar o ar e por simbolizar proteção.",
        "origem": "África",
        "cuidados": "Pouca água, resistente e ideal para ambientes internos."
    },

    # AQUÁTICAS
    {
        "nome": "Vitória-régia",
        "tipo": "Aquatica",
        "curiosidades": "Possui folhas gigantes que podem suportar peso.",
        "origem": "Amazônia",
        "cuidados": "Precisa de muita água e luz solar direta."
    },
    {
        "nome": "Lótus",
        "tipo": "Aquatica",
        "curiosidades": "Símbolo de pureza em várias culturas asiáticas.",
        "origem": "Ásia",
        "cuidados": "Água limpa, bastante luz e ambiente calmo."
    },
    {
        "nome": "Alface-d'água",
        "tipo": "Aquatica",
        "curiosidades": "Planta flutuante que ajuda a limpar a água.",
        "origem": "América Tropical",
        "cuidados": "Ambiente úmido, água limpa e temperatura estável."
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