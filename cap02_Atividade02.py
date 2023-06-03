from os import system
from random import randint
system('cls') # limpa a tela

print('***************************************')
print('****** Adivinhe qual é o número  ******')
print('***************************************')


# Relembrar constantes e variávies
numero_secreto = randint(0,100)

pontos = 1000
acerto = False

print('Qual o nível de dificuldade?')
print('(1) Padawan \n(2) Cavaleiro \n(3) Mestre Jedi ')
nivel = int(input('\nDefina o nível: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

pontos_a_perder = int(pontos / total_de_tentativas)
print(f'Sua pontuaçãoa atual: {pontos}')

for rodada in range (1, total_de_tentativas+1):
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
        break # interrrompe o laço
    else:
        pass #pass a diante
        # print('\nentrou no ELSE')
    finally:
        pass
        # print('\nentrou no FINALLY')

    if (tentativa_int < 1 or tentativa_int > 100):
        print('Tentativa inválida! Somente números de 1 a 100')
        rodada -= 1
        continue # volta no início do laço, ignorando o que está abaixo

    # segundo o guia de estilo para Python, é sempre, que possível, necessário melhorar 
    # a legibilidade do código.
    # Mudaremos o IF para uma  estrutura melhor

    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto

    # Nova estrututa de IFs
    if acerto:
        print(f'Boa tentativa. ACERTOU!!!! \nFez {pontos}!')
        #exit()
        break
    else:
        pontos_proximidade = 50 - abs(numero_secreto - tentativa_int)
        pontos = pontos - pontos_a_perder + pontos_proximidade
        print('Não foi dessa vez. ERROU!!!!')
        if ehmaior:
            print('Sua tentativa foi MAIOR que o número secreto.')
        if ehmenor:
            print('Sua tentativa foi MENOR que o número secreto.')
        if (rodada < total_de_tentativas):
            print(f'Sua pontuação atual: {pontos}')
        else:
            print('\n-----------------------------')
            print(f'O númeor secreto era {numero_secreto}')
            print(f'Sua pontuação final: {pontos}')
            print('-----------------------------')
            
        
if not acerto:
    print('GAME OVER!')
print('Obrigado por participar')