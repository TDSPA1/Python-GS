import os # para limpar a tela
import platform # para saber qual plataforma o usuario usa(Windows, mac OU Linux)
import random # para o embaralhamento da lista de perguntas

# "def limpar tela", tem como função limpar o terminal  a cada opção do usuário. Para utilizar esse comando precisei importar a biblioteca "os".
def limpar_tela():
    so = platform.system()
    if so == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
# as opções do menu principal
def menu_principal():
    print("BEM VINDO AO ECOCOSNCIENTE UM MUNDO EM MOVIMENTO VERDE.\n")
    print("[1] Gostaria de saber sobre as energias para um futuro melhor ?")
    print("[2] Venha testar seus conhecimento sobre as energias em um Quizzes.")
    print("[3] Gostaria de saber sobre os Obejtivos de Desenvolvimento Sustentável ?")
    print("[4] Encerrar.\n")

def escolha():  
    usuario_escolha = input("Qual das opções você gostaria de acessar ? ")
    limpar_tela()
    
    if usuario_escolha == "1":
        print("Que ótimo que você tem interesse em aprender sobre as energias! Isso é fundamental para a preservação da natureza e para construirmos um futuro mais sustentável.\n")
        print("[1] Energia renovável ?")
        print("[2] Energias não renováveis ?")
        print("[3] Gostaria de voltar para o menu principal ?\n")
        
        usuario_escolha = input("Qual das opções você gostaria ? ")
    
        if usuario_escolha == "1":
            limpar_tela()
            print("As energias renováveis são muito importante\n")
            print("[1] O que são energia renovável ?")
            print("[2] Quais são as energias renováveis ?")
            print("[3] Qual a importância da energia renovável ")
            print("[4] Qual a diferença entre energia renovável e não renovável ?")
            print("[5] Por que a energia renovável é tão crucial para o futuro do planeta ?")
            print("[6] Como adotar energia renovável em casa ou no negócio ?")
            print("[7] Gostaria de voltar para o menu principal ?\n")
            
            usuario_escolha = input("Qual dessas opções gostaria de acessar ? ")
            
            if usuario_escolha == "1":
                limpar_tela()
                print("Energia renovável é a energia proveniente de fontes naturais que se renovam constantemente, ou seja, não se esgotam com o tempo. Essas fontes de energia são mais sustentáveis e menos prejudiciais ao meio ambiente, pois produzem menos poluição e emissões de gases de efeito estufa")
                input("Pressione Enter para voltar para o menu principal")
                limpar_tela()
                menu_principal()
                escolha()
                
            elif usuario_escolha == "2":
                limpar_tela()
                print("As energias renováveis são:\n1. Energia solar: Gerada a partir da luz e calor do sol. Painéis solares convertem essa energia em eletricidade.\n2. Energia eólica:Proveniente do vento, que é convertido em eletricidade por turbinas eólicas.\n3. Energia hidrelétrica: Gerada a partir do movimento da água, geralmente por meio de barragens e quedas d'água.\n4. Energia biomassa: Produzida a partir da queima de matéria orgânica, como madeira, resíduos agrícolas ou até lixo, para gerar calor ou eletricidade\n5. Energia geotérmica: Derivada do calor do interior da Terra \n6. Energia maremotriz: é gerada a partir do movimento das marés, ou seja, o fluxo e refluxo das águas do mar\n7. Energia das ondas: é gerada a partir do movimento das ondas do mar. Esse tipo de energia aproveita a força do movimento das águas oceânicas, que resulta do vento, para gerar eletricidade. ")
                input("Pressione Enter para voltar para o menu principal")
                limpar_tela()
                menu_principal()
                escolha()
                
            elif usuario_escolha == "3":   
                limpar_tela()
                print("A energia renovável é fundamental para enfrentar os desafios ambientais, econômicos e sociais do mundo moderno. Ela oferece uma alternativa limpa, sustentável e segura para a geração de energia, ajudando a combater as mudanças climáticas, melhorar a qualidade do ar, promover a segurança energética e impulsionar o desenvolvimento econômico. Investir em fontes renováveis não é apenas uma necessidade ambiental, mas também uma oportunidade para criar um futuro mais justo, seguro e próspero para todos.:\n-Combate à poluição do ar e da água\n-Sustentabilidade e fontes inesgotáveis\n-Redução da dependência de combustíveis fósseis\n-Inovação e avanço tecnológico\n-Benefícios sociais e melhoria da qualidade de vida")
                input("Pressione Enter para voltar para o menu principal")
                limpar_tela()
                menu_principal()
                escolha()
                
            elif usuario_escolha == "4":
                limpar_tela()
                print("A diferença fundamental entre energia renovável e energia não renovável está relacionada à disponibilidade e ao impacto ambiental das fontes de energia\n-Energia renovavel: A energia renovável vem de fontes naturais que se renovam de forma contínua ou periódica, além das fontes de energia renovável tem um baixo impacto ambiental, Quando falamos em custo, a energia renovável acaba tendo um custo maior. ")
                print("Energia não renovável: A energia não renovável vem de fontes finitas, ou seja, elas não se renovam rapidamente ou se esgotam ao longo do tempo, e a queima de combustíveis fósseis (como carvão, petróleo e gás) libera grandes quantidades de CO₂ e outros poluentes, contribuindo para o aquecimento global, a poluição do ar e problemas de saúde. Além disso, a extração desses recursos pode causar dano ambiental significativo ")
                input("Pressione Enter para voltar para o menu principal")
                limpar_tela()
                menu_principal()
                escolha()
                
            elif usuario_escolha == "5":
                limpar_tela()
                print("A energia renovável é crucial para o futuro do planeta por várias razões que envolvem não apenas a sustentabilidade ambiental, mas também questões econômicas, sociais e de segurança energética. Com o mundo enfrentando desafios globais como as mudanças climáticas, a escassez de recursos fósseis e a poluição ambiental, a transição para fontes de energia renováveis se torna indispensável para garantir um futuro mais limpo, seguro e equilibrado.Algumas razões\n-Combate às Mudanças Climáticas\n-Redução da Poluição do Ar e da Água\n-Segurança Energética e Independência\n-Sustentabilidade a Longo Prazo")
                input("Pressione Enter para voltar para o menu principal")
                limpar_tela()
                menu_principal()
                escolha()
                
            elif usuario_escolha == "6":
                limpar_tela()
                print("Adotar energia renovável em casa ou no seu negócio é uma excelente maneira de reduzir a dependência de fontes de energia não renováveis, reduzir as emissões de carbono, diminuir os custos de energia e promover a sustentabilidade. Aqui estão algumas maneiras práticas de integrar fontes de energia renovável em sua residência ou empresa\n-Instalar Painéis Solares\n-Instalar Sistema de Energia Eólica\n-Implementar Sistemas de Armazenamento de Energia")
                input("Pressione Enter para voltar para o menu principal")
                limpar_tela()
                menu_principal()
                escolha()
                
            else:
                limpar_tela()
                menu_principal()
                escolha()
                
        elif usuario_escolha == "2" :
            limpar_tela()
            print("[1]O que são energia não renovável ?")
            print("[2]Quais são as energias não renováveis ?")
            print("[3]Qual a diferença entre energia renovável e não renovável ?")
            print("[4] Gostaria de voltar para o menu principal ?\n")
            
            usuario_escolha = input("Qual dessas opções gostaria de acessar ? ") 
            
            if usuario_escolha == "1":
                limpar_tela()
                print("A energia não renovável é aquela que provém de fontes naturais finitas, ou seja, recursos que se esgotam com o tempo e não se regeneram rapidamente, ao contrário das fontes de energia renováveis")
                input("Pressione Enter para voltar para o menu principal")
                limpar_tela()
                menu_principal()
                escolha()
                
            elif usuario_escolha == "2":
                limpar_tela()
                print("As principais fontes de energia não renovável são:\n-Petróleo\n-Carvão\n-Gás Natural\n-Energia Nuclear")
                input("Pressione Enter para voltar para o menu principal")
                limpar_tela()
                menu_principal()
                escolha()
                
            elif usuario_escolha == "3":
                limpar_tela() 
                print("A diferença fundamental entre energia renovável e energia não renovável está relacionada à disponibilidade e ao impacto ambiental das fontes de energia\n-Energia renovavel: A energia renovável vem de fontes naturais que se renovam de forma contínua ou periódica, além das fontes de energia renovável tem um baixo impacto ambiental, Quando falamos em custo, a energia renovável acaba tendo um custo maior.")
                print("Energia não renovável: A energia não renovável vem de fontes finitas, ou seja, elas não se renovam rapidamente ou se esgotam ao longo do tempo, e a queima de combustíveis fósseis (como carvão, petróleo e gás) libera grandes quantidades de CO₂ e outros poluentes, contribuindo para o aquecimento global, a poluição do ar e problemas de saúde. Além disso, a extração desses recursos pode causar dano ambiental significativo")
                input("Pressione Enter para voltar para o menu principal")
                limpar_tela()
                menu_principal()
                escolha()
                
            else:
                limpar_tela()
                menu_principal()
                escolha()
                
        else:
            limpar_tela()
            menu_principal()
            escolha()
            
    elif usuario_escolha == "2":
        limpar_tela()
        quizzes()
    elif usuario_escolha == "3":
        limpar_tela()
        print("Os Objetivos de Desenvolvimento Sustentável(ODS) são uma coleção de 17 metas globais, estabelecidas pela Assembleia Geral das Nações Unidas.\n")
        print("A partir dela, as nações trabalharão para cumprir os Objetivos de Desenvolvimento Sustentável. Os ODS representam um plano de ação global para eliminar a pobreza extrema e a fome, oferecer educação de qualidade ao longo da vida para todos, proteger o planeta e promover sociedades pacíficas e inclusivas até 2030.")
        print("\nAs 17 ODS são:\n-Erradicação da Pobreza\n-Fome Zero e Agricultura Sustentável\n-Saúde e Bem Estar\n-Educação de Qualidade\n-Igualdade de Gênero\n-Água Potável e Saneamento\n-Energia Acessível e Limpa\n-Trabalho Decente e Crescimento Econômico\n-Indústria, Inovação e Infraestrutura\n-Redução das Desigualdades\n-Cidades e Comunidades Sustentáveis\n-Consumo e Produção Responsáveis\n-Ação contra a Mudança Global do Clima\n-Vida na Água\n-Vida Terrestre\n-Paz, Justiça e Instituições Eficazes\n-Parcerias e Meios de Implementação ")
        input("Pressione Enter para voltar para o menu principal")
        limpar_tela()
        menu_principal()
        escolha()
    elif usuario_escolha == "4":
        limpar_tela()
        print("Encerrando o programa, até a próxima!!")
    else:
        print("opção inválida, por gentileza escolha uma opção de '1' ao '4'")
        menu_principal()
        escolha()
    
def quizzes():
    print("Bem-Vindo ao Quizzes, vamos testar seus conhecimentos !!! escolha uma opção como alternativa correta : ")
    nome_usuario = input("Digite seu nome ? ")
    print(f"Bom-Jogo, {nome_usuario} !! ")
    input("Aperte o enter para ir para o jogo")
    limpar_tela()
    pontuacao = 0 # para calcular a pontuacao do usuário
    
    # criei uma lista, para que cada vez que o usuário rodar o código as perguntas venham aleatorio, para ficar mais interativo o código
    perguntas = [ #primeiro a questao, altertiva e a resposta correta
        ("O que são energias renováveis?", [
            "A - Energia renovável são aquelas que se renovam naturalmente",
            "B - Energia renovável são aquelas que são produzidas pelo homem",
            "C - São energia gerada por fontes esgotáveis",
            "D - São energias consideradas poluentes"
        ], "a"),

        ("O que são energias não renováveis?", [
            "A - São energias encontradas na natureza e se renovam naturalmente",
            "B - São energia proveniente de fontes com recurso finito",
            "C - Causa pouco impacto para a natureza",
            "D - A superexploração das fontes faz com que os recursos não se esgotem rapidamente"
        ], "b"),

        ("Qual desses são considerados energia renovável?", [
            "A - Petróleo",
            "B - Gás Natural",
            "C - Carvão",
            "D - Luz Solar"
        ], "d"),

        ("Qual desses são considerados energia não renovável?", [
            "A - Carvão",
            "B - Água",
            "C - Energia solar",
            "D - Vento"
        ], "a"),

        ("Qual das alternativas é um benefício da energia eólica?", [
            "A - Causa grande impacto ambiental",
            "B - Não depende de condições climáticas para gerar eletricidade",
            "C - É uma fonte limpa e renovável de energia",
            "D - É uma energia não renovável"
        ], "c"),

        ("Essa fonte de energia muito utilizada no Brasil e no mundo é um minério fóssil que, quando processado, dá origem a vários subprodutos, como a gasolina, óleo diesel, querosene, além de gerar eletricidade nas usinas termoelétricas.", [
            "A - Gás natural",
            "B - Cana-de-açúcar",
            "C - Carvão mineral",
            "D - Petróleo"
        ], "d"),

        ("Avalie as questões a seguir que tratam das fontes de energia e sua importância:"
         "I) As fontes de energia exercem papel importante nas atividades humanas. Delas se originam eletricidade e combustíveis, que são úteis para a produção e transporte de bens e mercadorias."
         "II) São as fontes de energia mais utilizadas no Brasil: petróleo, hidrelétrica, carvão mineral e biocombustíveis."
         "III) A evolução das fontes de obtenção de energia teve impacto direto no trabalho humano. A energia facilitou e agilizou as atividades produtivas."
         "IV) No Brasil, as fontes de energia são prioritariamente as renováveis, como a energia eólica, energia solar e hidrelétrica"
         "Estão incorreta qual questão ?", [
            "A - I e IV",
            "B - II e III",
            "C - Apenas a alternativa III",
            "D - Apenas a alternativa IV"
        ], "d"),

        ("As fontes não renováveis podem se esgotar totalmente em prazos variáveis (pequeno, médio e longo prazo) de acordo com a extração, consumo e disponibilidade. Qual a resposta correta?", [
            "A - Biocombustíveis, petróleo e carvão mineral",
            "B - Energia solar, energia eólica e urânio",
            "C - Urânio, gás natural e energia hidrelétrica",
            "D - Energia hidrelétrica, energia solar e biocombustíveis"
        ], "a"),
        
        ("O que é a biomassa ?",[
            "A - Energia gerada a partir da fissão nuclear",
            "B - Energia gerada por processos geotérmicos",
            "C - Energia derivada de matéria orgânica",
            "D - Energia gerada a partir da queima de resíduos sólidos urbanos"   
        ], "c"),
        
        ("O que é o processo de fissão nuclear ?",[
            "A - Combustão de matéria orgânica para gerar eletricidade",
            "B - Quebra de átomos para liberar grandes quantidades de energia",
            "C - Processamento de resíduos de carvão"
            "D - Transformação de calor solar em eletricidade"    
        ], "b")
    ]
    
    random.shuffle(perguntas) #serve para embaralhar minha lista de perguntas, para que o quizzes fique mais interativo
    
    for pergunta, alternativas, resposta_correta in perguntas:
        print(f"\n{pergunta}\n")
        for alternativa in alternativas:
            print(alternativa)
            
        while True:
            usuario_resposta = input("\nQual é a resposta correta? (A/B/C/D): ").lower()
            if usuario_resposta in ["a","b","c","d"]: # se o usuário digitar uma das alternativa ele sai, da condicao do while e continua a questao, caso ele digite uma letra, que n seja (a,b,c ou d) ele ira para a condicao do else, onde irá pedir para ele digitar uma letra correta
                break
            else:
                print("\nResposta INVÁLIDA, por gentileza escolha uma opção entre (a/b/c/d)")
        
        if usuario_resposta == resposta_correta:
            print("\nResposta correta !!!")
            input("Pressione o enter para ir para a próxima questão")
            pontuacao += 1
        else:
            print("Resposta incorreta !!!")
            input("Pressione o enter para ir para a próxima questão")
        
        limpar_tela()


    print(f"\n{nome_usuario } sua pontuação final foi: {pontuacao} de {len(perguntas)}, obrigado por jogar")# len  quantidade de perguntas
    input("Pressione Enter para voltar para o menu principal")
    limpar_tela()
    menu_principal()
    escolha()
 

  
        
menu_principal()
escolha()