from os import system
#importa biblioteca do sistema
system('cls') #limpa tela para windows

print('***************************************')
print('****** Adivinhe qual é o número! ******')
print('***************************************')

# Definição de rodada inicial e o total de rodadas (tentativas)
# rodada = 1 - Para uso do FOR não é necessário a variável de contagem 
total_tentativas = 3

# Relembrar constantes e variávies
numero_secreto = 82 #constante

for rodada in range(1, total_tentativas + 1):
    print('\nTentativa {:02d} de {:02d}' . format(rodada, total_tentativas))
    tentativa = input('Tente acertar o número: ')
    print('Você digitou: ', tentativa)

    # é Preciso converte a string para int, de modo a haver comparação correta no if
    tentativa_int = int(tentativa)

    if (tentativa_int < 1 or tentativa_int > 100):
        print('Tentativa INVÁLIDA! Somente números entre 1 e 100!')
        continue
    # segundo o guia de estilo para Python, é sempre, que possível, necessário melhorar a legibilidade do código.
    # Mudaremos i IF para uma  estrutura melhor
    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto

    # Nova estrututa de IFs
    if acerto:
        print('Boa tentativa. ACERTOU!!!!')
        break #encerra o laço de repetição
    else:
        print('Não foi dessa vez. ERROU!!!!')
        if ehmaior:
            print('Sua tentativa foi MAIOR que o número secreto.')
        if ehmenor:
            print('Sua tentativa foi MENOR que o número secreto.')
    # rodada += 1 Para uso do FOR a variável de contagem é de auto incremento

print('Obrigado por participar')