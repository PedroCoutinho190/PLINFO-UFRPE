from utils.utilities import *

"""
Galeria de Plantas!
"""
plantas = [
    # MEDICINAIS
    {
        "nome": "🌵 Babosa",
        "tipo": "Medicinal",
        "curiosidades": """A babosa (Aloe vera) é uma planta suculenta, perene, pertencente à família Asphodelaceae. Apresenta folhas espessas, carnosas e dispostas em roseta, com bordas serrilhadas. Essas folhas armazenam água, caracterizando sua adaptação a ambientes áridos.

O interior das folhas contém um gel rico em compostos bioativos, como polissacarídeos, vitaminas e enzimas, amplamente estudados por suas propriedades medicinais e cicatrizantes.

Popularmente utilizada no tratamento de queimaduras, hidratação da pele e problemas gastrointestinais. Seu gel também é ingrediente comum em cosméticos, xampus e produtos farmacêuticos.""",
        "origem": """A espécie é originária de regiões de clima seco, especialmente do norte da África e da região do Mediterrâneo. Atualmente, encontra-se amplamente distribuída em áreas tropicais e subtropicais ao redor do mundo, incluindo o Brasil.

Foi introduzida na América Latina pelos colonizadores europeus e rapidamente se adaptou ao clima quente e seco de regiões como o Nordeste brasileiro.""",
        "cuidados": """A babosa apresenta baixa exigência de manutenção, mas requer condições específicas para bom desenvolvimento:

- Necessita de alta luminosidade ou sol pleno
- Deve ser cultivada em solo bem drenado, preferencialmente arenoso
- A irrigação deve ser moderada, evitando encharcamento
- É sensível a baixas temperaturas e geadas
- As folhas mais velhas e secas devem ser removidas periodicamente
- Adubação leve a cada 2 meses durante o verão favorece o crescimento

O excesso de água é o principal fator de risco, podendo causar apodrecimento das raízes.""",
        "reflorestamento": """A babosa pode ser utilizada em projetos de recuperação de áreas degradadas, especialmente em regiões semiáridas e de Caatinga, onde o solo é pobre e seco.

Sua resistência à seca e capacidade de proteger o solo contra erosão fazem dela uma aliada importante em reflorestamentos de zonas áridas. Além disso, atrai insetos polinizadores quando em floração, contribuindo para a biodiversidade local.

No contexto do bioma Caatinga, sua presença ajuda a reter umidade no solo e criar microambientes favoráveis para outras espécies vegetais.""",
        "cultivo": """Pode ser cultivada facilmente em vasos com boa drenagem, bastante luz solar e pouca rega. É uma das plantas mais indicadas para iniciantes.

- Utilize vasos com furos no fundo para evitar acúmulo de água
- O substrato ideal é uma mistura de terra, areia grossa e cascalho
- Regue apenas quando o solo estiver completamente seco
- Pode ser propagada por filhotes que nascem na base da planta
- Em vasos pequenos, transplante quando as raízes começarem a sair pelos furos

É uma excelente opção para jardins de baixo consumo de água e hortas medicinais domésticas."""
    },

    {
        "nome": "🍃 Hortelã",
        "tipo": "Medicinal",
        "curiosidades": """A hortelã (Mentha spp.) é uma planta aromática herbácea pertencente à família Lamiaceae. Possui folhas ovais com bordas dentadas e aroma intenso e refrescante devido ao mentol, seu principal composto ativo.

É amplamente utilizada na culinária, na medicina natural e na indústria farmacêutica. Possui propriedades digestivas, antiespasmódicas, analgésicas e antimicrobianas. Seu chá é indicado para aliviar cólicas, náuseas, dores de cabeça e congestão nasal.

Existem diversas espécies e híbridos de hortelã, como a hortelã-pimenta (Mentha piperita) e a hortelã-verde (Mentha spicata), cada uma com características aromáticas distintas.""",
        "origem": """Originária da Europa e da Ásia, a hortelã foi utilizada por gregos e romanos na antiguidade tanto como tempero quanto como remédio. Se adaptou facilmente a diferentes regiões do mundo, sendo hoje amplamente cultivada em climas temperados e tropicais.

No Brasil, foi introduzida pelos colonizadores e se naturalizou em diversas regiões, sendo cultivada tanto em pequenas hortas domésticas quanto em escala comercial.""",
        "cuidados": """A hortelã cresce com facilidade, mas requer alguns cuidados:

- Prefere locais com meia sombra ou sol da manhã
- Solo deve ser úmido, fértil e rico em matéria orgânica
- Regas frequentes, sem deixar o solo secar completamente
- Pode se espalhar rapidamente por estolões subterrâneos
- Recomenda-se cultivar em vasos para controlar o crescimento
- A poda regular estimula o brotamento e mantém a planta produtiva
- Adubação orgânica a cada 30 dias melhora o rendimento""",
        "reflorestamento": """A hortelã contribui para a biodiversidade ao atrair abelhas, borboletas e outros insetos polinizadores com suas flores. Pode ser utilizada como planta de cobertura em solos úmidos, ajudando a controlar ervas daninhas e proteger o solo da erosão.

Em projetos agroflorestais, é usada como planta companheira, afastando pragas de outras culturas devido ao seu aroma intenso. Não é indicada para reflorestamentos de matas nativas, mas tem papel importante em sistemas agroflorestais e hortas comunitárias.""",
        "cultivo": """Muito fácil de cultivar em vasos ou canteiros. Cresce rapidamente e produz bastante.

- Prefira vasos médios ou grandes, pois as raízes se expandem muito
- Use substrato rico em matéria orgânica e mantenha sempre úmido
- Pode ser propagada por estacas: corte um ramo, coloque em água e espere enraizar
- Faça podas regulares para evitar que a planta fique muito alta e ramificada
- Evite cultivar junto de outras plantas em canteiros abertos, pois pode sufocar vizinhas
- A colheita pode ser feita cortando os galhos assim que a planta tiver pelo menos 15 cm"""
    },

    {
        "nome": "🌼 Camomila",
        "tipo": "Medicinal",
        "curiosidades": """A camomila (Matricaria chamomilla) é uma planta herbácea anual da família Asteraceae, reconhecida por suas pequenas flores brancas com centro amarelo e aroma suave e adocicado.

É uma das plantas medicinais mais antigas e utilizadas no mundo. Seu principal uso é como calmante natural, sendo indicada para ansiedade, insônia e estresse. Também possui propriedades anti-inflamatórias, antiespasmódicas e cicatrizantes, sendo usada em chás, extratos e cosméticos.

Seus compostos ativos incluem o azuleno, a apigenina e o bisabolol, responsáveis por seus efeitos terapêuticos.""",
        "origem": """Originária da Europa Central e da Ásia Ocidental, a camomila era amplamente utilizada na medicina popular egípcia, grega e romana. Foi introduzida no Brasil por imigrantes europeus e hoje é cultivada comercialmente em estados como São Paulo e Paraná.

Adapta-se bem a climas amenos e temperados, sendo uma das plantas medicinais mais cultivadas no mundo.""",
        "cuidados": """Para um bom cultivo:

- Necessita de sol moderado, de preferência sol da manhã
- Solo leve, arenoso e bem drenado
- Regas regulares, evitando excesso de água e encharcamento
- Prefere climas amenos, com temperaturas entre 15°C e 25°C
- Sensível ao calor excessivo, que pode encurtar seu ciclo de vida
- Retirar flores murchas estimula o surgimento de novas flores
- Não necessita de adubação intensa; excesso de nitrogênio reduz a floração""",
        "reflorestamento": """A camomila tem papel importante como planta de cobertura em solos degradados de regiões de clima temperado. Suas raízes ajudam a soltar o solo compactado e sua presença atrai polinizadores essenciais ao ecossistema.

É utilizada em sistemas agroflorestais como planta companheira, beneficiando culturas vizinhas ao melhorar o solo e afastar alguns insetos nocivos. Apesar de não ser nativa do Brasil, pode ser integrada a projetos de recuperação de áreas em regiões de altitude mais elevada.""",
        "cultivo": """Pode ser cultivada em vasos pequenos ou canteiros com boa iluminação.

- Semeie diretamente no solo ou em bandejas de mudas
- As sementes são muito pequenas; misture com areia para distribuir melhor
- Germinação ocorre entre 7 e 14 dias em temperatura ambiente
- Transplante as mudas quando tiverem cerca de 5 cm de altura
- Floresce em aproximadamente 60 dias após o plantio
- A colheita das flores deve ser feita logo após a abertura completa, para preservar os compostos ativos
- Ideal para hortas medicinais domésticas e jardins aromáticos"""
    },

    # VENENOSAS
    {
        "nome": "💀 Comigo-ninguém-pode",
        "tipo": "Venenosa",
        "curiosidades": """A comigo-ninguém-pode (Dieffenbachia spp.) é uma planta ornamental tropical da família Araceae. Possui folhas largas e variegadas, com padrões de verde e branco ou amarelo, o que a torna muito popular na decoração de interiores.

Apesar da beleza, é altamente tóxica. Suas folhas e caules contêm cristais de oxalato de cálcio e outras substâncias irritantes que, ao serem mastigados ou ingeridos, causam queimação intensa, inchaço da língua e garganta, dificuldade de falar e engolir, e em casos graves, obstrução das vias aéreas.

O nome popular faz referência justamente a esse efeito: quem ingere a planta fica temporariamente sem conseguir falar.""",
        "origem": """Originária das regiões tropicais da América do Sul e Central, especialmente de florestas úmidas do Brasil, Colômbia e Costa Rica. Foi amplamente difundida como planta ornamental ao redor do mundo devido à sua beleza e resistência.""",
        "cuidados": """Apesar de resistente, exige atenção por sua toxicidade:

- Manter fora do alcance de crianças e animais domésticos
- Usar luvas ao manusear ou podar a planta
- Evitar contato da seiva com olhos e mucosas
- Prefere ambientes internos com luz indireta e difusa
- Regas moderadas, deixando o solo secar levemente entre elas
- Umidade ambiente elevada favorece o crescimento
- Limpeza das folhas com pano úmido melhora a absorção de luz""",
        "reflorestamento": """Não é indicada para projetos de reflorestamento de matas nativas devido à sua toxicidade para a fauna local e por ser uma espécie exótica em muitas regiões.

Seu uso é restrito a ambientes ornamentais e urbanos. Em grandes quantidades, pode impactar negativamente animais silvestres que eventualmente a consumam.""",
        "cultivo": """Pode ser cultivada em ambientes internos com facilidade, mas exige cuidados de segurança.

- Utilize vasos com boa drenagem e substrato leve
- Posicione em locais com luminosidade indireta, longe de janelas com sol direto
- Regue moderadamente, sem encharcar o solo
- Adubar a cada 2 meses com adubo para folhagens
- Pode ser propagada por corte do caule, que deve ser plantado em substrato úmido
- Sempre lave as mãos após manusear a planta
- Sinalize em casa sobre sua toxicidade para evitar acidentes"""
    },

    {
        "nome": "🫘  Mamona",
        "tipo": "Venenosa",
        "curiosidades": """A mamona (Ricinus communis) é uma planta arbustiva da família Euphorbiaceae, podendo atingir até 3 metros de altura. Possui folhas grandes e palmatífidas, de coloração verde ou avermelhada, e frutos espinhosos que contêm as sementes.

Suas sementes produzem o óleo de rícino, amplamente utilizado na indústria farmacêutica, cosmética e como biocombustível. No entanto, as sementes contêm ricina, uma das substâncias mais tóxicas conhecidas na natureza, capaz de causar morte em pequenas doses se ingerida.

A intoxicação por mamona pode causar náuseas, vômitos, diarreia severa, falência de órgãos e morte.""",
        "origem": """Originária do nordeste da África e do Oriente Médio, a mamona foi difundida pelo mundo por sua utilidade industrial. No Brasil, é cultivada especialmente no Nordeste, onde se adapta bem ao clima semiárido e é usada na produção de biodiesel.""",
        "cuidados": """Cuidados importantes no manuseio e cultivo:

- Nunca ingerir sementes ou qualquer parte da planta
- Usar equipamentos de proteção ao manusear
- Manter longe de crianças e animais
- Prefere sol pleno e solo bem drenado
- Tolerante à seca, não necessita de irrigação frequente
- Crescimento rápido; pode necessitar de suporte para os galhos
- Evitar cultivo próximo a hortas de alimentos""",
        "reflorestamento": """A mamona é utilizada em programas de recuperação de solos degradados no semiárido brasileiro, especialmente por sua tolerância à seca e crescimento rápido, que ajudam a proteger o solo da erosão.

No entanto, seu uso em reflorestamentos deve ser feito com cautela, pois sua toxicidade pode impactar a fauna local. É mais indicada como cultura de cobertura temporária do que como espécie permanente em ecossistemas naturais.""",
        "cultivo": """Não é recomendada para cultivo doméstico em locais com circulação de crianças ou animais.

- Plante em locais isolados, com boa insolação e solo fértil
- A semeadura é feita diretamente no solo, em covas de 3 a 5 cm de profundidade
- Germinação ocorre entre 7 e 15 dias
- Espaçamento mínimo de 1 metro entre plantas
- Não necessita de adubação intensa em solos razoavelmente férteis
- A colheita dos frutos deve ser feita com luvas antes que se abram espontaneamente
- Descarte correto das partes da planta é essencial para evitar contaminação"""
    },

    {
        "nome": "🗡️  Espada-de-são-jorge",
        "tipo": "Venenosa",
        "curiosidades": """A espada-de-são-jorge (Sansevieria trifasciata) é uma planta suculenta da família Asparagaceae, conhecida por suas folhas longas, rígidas e pontiagudas, com listras horizontais em tons de verde e amarelo.

É amplamente utilizada como planta ornamental e purificadora do ar, sendo capaz de absorver compostos tóxicos como formaldeído e benzeno do ambiente. Na cultura popular brasileira, é associada à proteção espiritual e afastamento de energias negativas.

Apesar de seus benefícios, contém saponinas em todas as suas partes, substâncias tóxicas que podem causar náuseas, vômitos e diarreia se ingeridas por humanos ou animais.""",
        "origem": """Originária da África Ocidental, especialmente do oeste da Nigéria ao Congo. Foi introduzida em todo o mundo como planta ornamental e hoje é encontrada em praticamente todos os países tropicais e subtropicais.""",
        "cuidados": """Extremamente resistente e de fácil manutenção:

- Tolera ambientes com pouca luz, mas cresce melhor com luz indireta
- Regas muito espaçadas; aguarde o solo secar completamente antes de regar
- Sensível ao excesso de água, que apodrece as raízes rapidamente
- Evitar contato de crianças e animais com as folhas e raízes
- Não requer adubação frequente; uma vez por ano é suficiente
- Resistente a variações de temperatura e baixa umidade
- Limpeza das folhas com pano úmido mantém a planta saudável e bonita""",
        "reflorestamento": """Por ser uma espécie exótica, não é indicada para reflorestamentos de biomas nativos brasileiros. Seu uso é voltado principalmente para ambientes urbanos, como jardins, calçadas e espaços internos.

Em algumas regiões, pode se comportar como invasora se introduzida em ambientes naturais, competindo com espécies nativas. Projetos de revegetação urbana, no entanto, podem se beneficiar de sua resistência e baixa manutenção.""",
        "cultivo": """Uma das plantas mais fáceis de cultivar, ideal para iniciantes e ambientes internos.

- Pode ser cultivada em vasos pequenos ou grandes, com substrato bem drenado
- Suporta longos períodos sem rega, sendo ideal para quem viaja com frequência
- Propaga-se facilmente por divisão de touceiras ou corte de folhas
- Para propagar por folha: corte em segmentos de 10 cm e plante na vertical em substrato seco
- Evite vasos sem drenagem, pois o acúmulo de água é seu principal inimigo
- Pode ser cultivada em ambientes com ar-condicionado sem problemas
- Troque de vaso apenas quando as raízes estiverem saindo pelos furos"""
    },

    # AQUÁTICAS
    {
        "nome": "🪷  Vitória-régia",
        "tipo": "Aquatica",
        "curiosidades": """A vitória-régia (Victoria amazonica) é uma planta aquática da família Nymphaeaceae e um dos maiores símbolos da flora amazônica. Suas folhas circulares podem atingir até 3 metros de diâmetro e suportar cargas de até 40 kg devido a uma estrutura de nervuras semelhante a uma treliça.

Suas flores, que duram apenas dois dias, mudam de cor branca para rosa ao longo do ciclo de floração e exalam um aroma adocicado que atrai besoiros polinizadores. É um dos maiores e mais impressionantes exemplares do reino vegetal.

Inspirou o design arquitetônico do Crystal Palace de Joseph Paxton, construído em Londres em 1851.""",
        "origem": """Originária da bacia amazônica, ocorre naturalmente em lagos e rios de águas calmas da Amazônia brasileira, boliviana e de países vizinhos. Foi descrita cientificamente no século XIX e rapidamente se tornou símbolo de exotismo e grandiosidade da natureza tropical.""",
        "cuidados": """Necessita de condições muito específicas para sobreviver:

- Requer grandes volumes de água limpa e aquecida, entre 25°C e 35°C
- Exposição plena ao sol por pelo menos 6 horas diárias
- Ambiente quente, úmido e sem ventos fortes
- Espaço amplo: cada planta pode ocupar até 10 m² de superfície aquática
- A água deve ser levemente fertilizada com nutrientes específicos para aquáticas
- Não tolera poluição ou variações bruscas de temperatura""",
        "reflorestamento": """A vitória-régia é fundamental para a manutenção de ecossistemas aquáticos amazônicos. Suas folhas criam sombra sobre a água, regulando a temperatura e reduzindo o crescimento excessivo de algas.

Serve de abrigo e local de reprodução para peixes, insetos e anfíbios. Em projetos de restauração de lagos e igapós amazônicos, sua reintrodução é considerada indicadora de saúde do ecossistema aquático. Sua preservação está diretamente ligada à conservação do bioma amazônico.""",
        "cultivo": """Extremamente difícil de cultivar fora de seu ambiente natural.

- Requer reservatórios com no mínimo 1,5 m de profundidade e vários metros de diâmetro
- A temperatura da água deve ser mantida entre 25°C e 35°C constantemente
- O substrato deve ser argiloso e rico em matéria orgânica
- A semeadura é feita com sementes frescas, mantidas em água morna
- Germinação ocorre entre 2 e 4 semanas
- Não é viável para cultivo doméstico convencional
- Encontrada em jardins botânicos e parques aquáticos com estrutura especializada"""
    },

    {
        "nome": "🌸 Lótus",
        "tipo": "Aquatica",
        "curiosidades": """O lótus (Nelumbo nucifera) é uma planta aquática sagrada em diversas culturas asiáticas, especialmente no hinduísmo e no budismo, onde simboliza pureza, iluminação e renascimento. Suas flores emergem intactas e limpas da lama, o que inspira seu simbolismo espiritual.

Possui propriedades autolimpantes nas folhas, conhecidas como efeito lótus, que repelem água e sujeira. Suas sementes têm longevidade extraordinária: sementes com mais de 1.300 anos já foram germinadas com sucesso em laboratório.

Todas as partes da planta são comestíveis e utilizadas na culinária asiática, além de possuírem propriedades medicinais reconhecidas.""",
        "origem": """Originária da Ásia, especialmente da Índia, China e sudeste asiático. É cultivada há milênios nessas regiões tanto para fins religiosos quanto alimentares e medicinais. Hoje é encontrada em jardins aquáticos ao redor do mundo.""",
        "cuidados": """Para um cultivo saudável:

- Necessita de água limpa, parada ou de fluxo lento
- Exposição plena ao sol, pelo menos 6 horas diárias
- Solo lodoso e rico em nutrientes no fundo do recipiente
- Temperatura da água entre 20°C e 30°C
- Não tolera frio intenso; em regiões frias, o rizoma deve ser protegido no inverno
- Remoção de folhas e flores murchas estimula novo crescimento
- Adubação específica para plantas aquáticas a cada 30 dias""",
        "reflorestamento": """O lótus contribui para o equilíbrio de ecossistemas aquáticos ao oxigenar a água, fornecer abrigo para pequenos animais aquáticos e servir de alimento para aves e peixes.

Em projetos de recuperação de lagos e tanques degradados, pode ser utilizado para melhorar a qualidade da água e restaurar a biodiversidade aquática local. Por ser uma espécie exótica no Brasil, seu uso em ambientes naturais deve ser avaliado com cuidado para evitar impactos sobre espécies nativas.""",
        "cultivo": """Pode ser cultivado em tanques, bacias grandes ou lagos artificiais.

- Use recipientes com pelo menos 40 cm de profundidade e 60 cm de diâmetro
- Coloque uma camada de 10 a 15 cm de argila ou substrato aquático no fundo
- Plante o rizoma horizontalmente, com a ponta para cima, a cerca de 5 cm de profundidade
- Adicione água lentamente para não deslocar o substrato
- Posicione em local com sol pleno
- As primeiras folhas flutuantes aparecem em 2 a 3 semanas
- A floração ocorre no verão, em plantas com pelo menos um ano de cultivo"""
    },

    {
        "nome": "🥬 Alface-d'água",
        "tipo": "Aquatica",
        "curiosidades": """A alface-d'água (Pistia stratiotes) é uma planta aquática flutuante da família Araceae, com folhas verde-claras, aveludadas e dispostas em roseta, semelhantes a uma alface em miniatura.

É uma excelente filtradora natural da água, absorvendo nutrientes em excesso como nitrogênio e fósforo, o que a torna valiosa em sistemas de fitorremediação e no tratamento natural de efluentes. Também serve de abrigo e alimento para peixes e pequenos invertebrados aquáticos.

Apesar de seus benefícios, pode se tornar invasora em ambientes naturais, cobrindo toda a superfície da água e impedindo a passagem de luz, o que sufoca outras formas de vida aquática.""",
        "origem": """Ocorre naturalmente em regiões tropicais e subtropicais das Américas, África e Ásia. No Brasil, é encontrada em lagos, rios de curso lento e áreas alagadas de diversas regiões, sendo considerada nativa em parte do território nacional.""",
        "cuidados": """Cuidados básicos para cultivo controlado:

- Necessita de água limpa ou levemente turva
- Boa iluminação, preferencialmente sol direto
- Temperatura da água entre 20°C e 30°C
- Controle rigoroso do crescimento, pois se multiplica rapidamente
- Remoção periódica do excesso de plantas para evitar cobertura total da superfície
- Em aquários, pode necessitar de fertilização líquida leve
- Não misturar com espécies aquáticas pequenas que possam ser sufocadas""",
        "reflorestamento": """A alface-d'água tem papel importante na purificação de corpos d'água degradados por excesso de nutrientes (eutrofização), sendo utilizada em projetos de fitorremediação em lagos e lagoas poluídas.

Auxilia na restauração de ecossistemas aquáticos ao melhorar a qualidade da água e criar condições favoráveis para o retorno de fauna aquática. No entanto, seu uso deve ser monitorado, pois em ambientes sem controle natural pode se tornar invasora e prejudicar a biodiversidade local.""",
        "cultivo": """Fácil de cultivar em aquários, tanques e fontes decorativas.

- Simplesmente coloque as plantas na superfície da água; não precisam de substrato
- A água deve estar limpa e com boa iluminação
- Se multiplicam por emissão de estolões laterais; remova o excesso regularmente
- Em aquários, contribuem para a qualidade da água absorvendo nutrientes
- Podem ser usadas em sistemas de aquaponia, auxiliando no equilíbrio do ecossistema
- Em recipientes fechados, verifique se não estão bloqueando toda a luz da água
- No inverno, em regiões frias, as plantas podem morrer, mas rebrotam com o calor"""
    }
]    
    

def galeria_menu():
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