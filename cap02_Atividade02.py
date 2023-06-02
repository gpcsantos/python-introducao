from os import system
system('cls') # limpa a tela

print('***************************************')
print('****** Adivinhe qual é o número  ******')
print('***************************************')


# Relembrar constantes e variávies
numero_secreto = 83 #constante

rodada = 0
total_de_tentativas = 3
acerto = False

while (rodada <= total_de_tentativas):
    rodada += 1
    tentativa = input('Tente acertar o número: ')
    print('Você digitou: ', tentativa)
    print(f'\nTentativa {rodada:02d} de {total_de_tentativas:02d}')
    
    # é Preciso converte a string para int, de modo a haver comparação correta no if
    try: 
        tentativa_int = int(tentativa)
    except ValueError:
        print('Valor inválido. Informe um número inteiro')
        break
    except Exception as e:
        print(f'ERRO: {e}')
        break
    else:
        pass
        # print('\nentrou no ELSE')
    finally:
        pass
        # print('\nentrou no FINALLY')

    # segundo o guia de estilo para Python, é sempre, que possível, necessário melhorar 
    # a legibilidade do código.
    # Mudaremos o IF para uma  estrutura melhor

    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto

    # Nova estrututa de IFs
    if acerto:
        print('Boa tentativa. ACERTOU!!!!')
        #exit()
        break
    else:
        print('Não foi dessa vez. ERROU!!!!')
        if ehmaior:
            print('Sua tentativa foi MAIOR que o número secreto.')
        if ehmenor:
            print('Sua tentativa foi MENOR que o número secreto.')
        
if not acerto:
    print('GAME OVER!')
print('Obrigado por participar')