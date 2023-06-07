from random import randint
from desenhos import forca, vencedor, perdedor
from os import system
system('cls') 

def imprime_abertura():
    print("*" * 28)
    print(" Jogo da forca ".center(28,"-"))
    print("*" * 28)

def carrega_palavra_secreta():
    arquivo = open('txt/frutas.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    sorteio = randint(0, len(palavras))

    palavra_secreta = palavras[sorteio].upper()
    return palavra_secreta

def init_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def verifica_letra_repetida(letras_acertas, letra):
    return letra in letras_acertas
        
def gg():
    
    imprime_abertura()
   
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = init_letras_acertadas(palavra_secreta)
    letras_tentativas = []

    morreu = False
    acertou = False
    erros = 0

    while(not morreu and not acertou):
        tentativa = input('Qual a letra? ').strip().upper()
        
        if verifica_letra_repetida(letras_tentativas, tentativa):
            print(f'A Letra {tentativa} já foi utilizada!')
            continue
        
        letras_tentativas.append(tentativa)

        index = 0
        if tentativa in palavra_secreta:
            for letra in palavra_secreta:
                if (tentativa ==  letra):
                    #print(f'Encontrei a letra {letra} na posição {index}')
                    letras_acertadas[index] = letra

                index += 1
            print(f'Seus acertos: {letras_acertadas}')
        else:
            erros += 1
            morreu = erros == 7
            forca(erros)
        
        acertou = '_' not in letras_acertadas
        print(f'Suas tentativas: {letras_tentativas}')

    if acertou:
        vencedor()
    else:
        perdedor(palavra_secreta)
        
       
    print('GG forca')

    print('\nObrigado por participar!\n')

if __name__ == '__main__':
    gg()
