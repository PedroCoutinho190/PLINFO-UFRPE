from utils.utilities import *
from plantas_data.lista_planta import plantas

def galeria_menu():
    """
    Galeria de Plantas!
    """

    while True:

        clear_screen()

        print(colorir("=" * 45, Fore.GREEN))
        print(colorir("🌿 GALERIA DE PLANTAS 🌿".center(45), Fore.GREEN))
        print(colorir("=" * 45, Fore.GREEN))
        print()

        for i, planta in enumerate(plantas):
            print(
                colorir(f" [{i+1}] ", Fore.CYAN) +
                f"{planta['nome']} " +
                colorir(f"({planta['tipo']})", Fore.YELLOW)
            )

        print(colorir(" [0] ", Fore.CYAN) + "Voltar")

        print()
        print(colorir("=" * 45, Fore.GREEN))

        entrada = input("-> Escolha a Planta: ").strip()

        if not entrada.isdigit():
            print(colorir("Digite apenas números!", Fore.RED))
            input("Pressione ENTER...")
            continue

        escolha = int(entrada)

        if escolha == 0:
            break

        if escolha < 1 or escolha > len(plantas):
            print(colorir("Opção inválida! ❌", Fore.RED))
            input("Pressione ENTER...")
            continue

        planta = plantas[escolha - 1]

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
            print(colorir(" [0] ", Fore.CYAN) + "↩️ Voltar")

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
                print("\n📌 Curiosidades:\n", planta["curiosidades"])
            elif info == 2:
                print("\n🌍 Origem:\n", planta["origem"])
            elif info == 3:
                print("\n💧 Cuidados:\n", planta["cuidados"])
            elif info == 4:
                print("\n🌳 Reflorestamento:\n", planta["reflorestamento"])
            elif info == 5:
                print("\n🏡 Cultivo em casa:\n", planta["cultivo"])
            else:
                print(colorir("Opção inválida! ❌", Fore.RED))

            input("\nPressione ENTER para continuar...")