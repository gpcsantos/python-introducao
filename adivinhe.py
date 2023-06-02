import random

def gg():

    print('***************************************')
    print('****** Adivinhe qual é o número! ******')
    print('***************************************')

    numero_secreto = random.randint(0,101)
    total_tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Padawan \n(2) Cavalheiro \n(3) Mestre Jedi')

    nivel = int(input('\nDefina o nível: '))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        # elif é usado quando temos mais critários e escolhas dentro de um if
        total_tentativas = 10
    else:
        total_tentativas = 5

    pontos_a_perder = int(pontos / total_tentativas)
    print('Sua pontuação atual: {}' . format(pontos))

    for rodada in range(1, total_tentativas + 1):
        print('\nTentativa {:02d} de {:02d}' . format(rodada, total_tentativas))
        tentativa = int(input('Tente acertar o número entre 1 e 100: '))
        print('Você digitou: ', tentativa)

        if (tentativa < 1 or tentativa > 100):
            print('Tentativa INVÁLIDA! Somente números entre 1 e 100!')
            continue
        # segundo o guia de estilo para Python, é sempre, que possível, necessário melhorar a legibilidade do código.
        # Mudaremos i IF para uma  estrutura melhor
        acerto = tentativa == numero_secreto
        ehmaior = tentativa > numero_secreto
        ehmenor = tentativa < numero_secreto

        # Nova estrututa de IFs
        if acerto:
            print('Boa tentativa. ACERTOU!!!! Fez {} pontos' . format(pontos))
            break #encerra o laço de repetição
        else:
            pontos_proximidade = 50 - abs(numero_secreto - tentativa)
            pontos = (pontos - pontos_a_perder + pontos_proximidade)
            print('Não foi dessa vez. ERROU!!!!')
            if ehmaior:
                print('Sua tentativa foi MAIOR que o número secreto.')
            elif ehmenor:
                print('Sua tentativa foi MENOR que o número secreto.')
            if(rodada < total_tentativas):
                print('Sua pontuação atual: {}' . format(pontos))
            else:
                print('\n------------------------------------')
                print('O número secreto era {}' . format(numero_secreto))
                print('Sua pontuação FINAL: {}' . format(pontos))
                print('GAME OVER')
                print('------------------------------------')
        
    print('Obrigado por participar')


if(__name__ == "__main__"):
    gg()
