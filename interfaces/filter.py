from utils.utilities import *
from plantas_data.lista_planta import plantas

def filter_menu():
    """
    Filtro de Plantas!
    """

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
                print(colorir(" [4] ", Fore.CYAN) + "🌳 Reflorestamento")
                print(colorir(" [5] ", Fore.CYAN) + "🏡 Cultivo em casa")
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
                elif info == 4:
                    print("\n🌳", planta["reflorestamento"])
                elif info == 5:
                    print("\n🏡", planta["cultivo"])                
                else:
                    print(colorir("Opção inválida! ❌", Fore.RED))

                input("\nPressione ENTER para continuar...")
                