print('***************************************')
print('****** Adivinhe qual é o número  ******')
print('***************************************')


# Relembrar constantes e variávies
NUMERO_SECRETO = 83 #constante
tentativa = input('Tente acertar o número: ')
print('Você digitou: ', tentativa)

# é Preciso converte a string para int, de modo a haver comparação correta no if
try: 
    tentativa_int = int(tentativa)
except ValueError:
    print('Valor inválido. Informe um número inteiro')
    exit()
except Exception as e:
    print(f'ERRO: {e}')
    exit()
else:
    print('\nentrou no ELSE')
finally:
    print('\nentrou no FINALLY')

# Relembrando estrutura de decisão
# Aproveitamos para falar de identação (4 espaços ou tab)
# Identação é parte do código Python e faz total diferança em código
if (NUMERO_SECRETO == tentativa_int):
    print("Boa tentativa. ACERTOU!")
else:
    print('Não foi dessa vez. ERROU!')

#finalização do GAME
print('GAME OVER!')
print('Obrigado por participar!')


