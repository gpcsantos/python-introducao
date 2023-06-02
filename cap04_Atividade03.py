from random import randrange

def imprime_abertura():
    print("*" * 28)
    print(" Jogo da forca ".center(28,"-"))
    print("*" * 28)

def carrega_palavra_secreta():
    arquivo = open('frutas.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = randrange(0, len(palavras)+1)
    
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def init_letras_acertadas(palavra_secreta):
    # letras_acertadas = ["_" for letra in palavra_secreta]
    # return letras_acertadas
    return ["_" for letra in palavra_secreta]

def gg():
    # def nome_funcao(), cria uma função, basta identar o código para inserir ações
    
    imprime_abertura()

    palavra_secreta = carrega_palavra_secreta()
    # palavra_secreta = 'banana'.upper()
    # letras_acertadas = ["_","_","_","_","_","_"]

    # for letra in palavra_secreta:
    #     letras_acertadas.append('_')

    #usando list comprehension
    letras_acertadas = init_letras_acertadas(palavra_secreta)

    morreu = False
    acertou = False
    erros = 0

    # enquanto não morreu E não acertou 
    # enquanto não False
    # enquanto (True)

    while(not morreu and not acertou):
        tentativa = input('Qual a letra? ').strip().upper()

        if (tentativa in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (tentativa ==  letra):
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)
        else:
            erros += 1
            morreu = erros == 7
            
        acertou = "_" not in letras_acertadas
        
        if (acertou):
            print('Venceu!')
        else:
            print('Perdeu!')
        
        print('GG forca')

    print('\nObrigado por participar!\n')





if (__name__ == "__main__"):
    gg()
        
