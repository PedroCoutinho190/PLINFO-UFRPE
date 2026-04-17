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

def galeria_menu():
    while True:

        clear_screen()

        print(colorir("=" * 45, Fore.GREEN))
        print(colorir("🌿 GALERIA DE PLANTAS 🌿".center(45), Fore.GREEN))
        print(colorir("=" * 45, Fore.GREEN))
        print()

        # lista bonita
        for i, planta in enumerate(plantas):
            print(
                colorir(f" [{i+1}] ", Fore.CYAN) +
                f"{planta['nome']} " +
                colorir(f"({planta['tipo']})", Fore.YELLOW)
            )

        print(colorir(" [0] ", Fore.CYAN) + "Voltar")

        print()
        print(colorir("=" * 45, Fore.GREEN))

        # 🔥 tratamento de erro
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

        # submenu bonito
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