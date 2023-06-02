

def gg():
    # def nome_funcao(), cria uma função, basta identar o código para inserir ações
    print("*" * 28)
    print(" Jogo da forca ".center(28,"-"))
    print("*" * 28)
    
    palavra_secreta = 'banana'.upper()
    # letras_acertadas = ["_","_","_","_","_","_"]

    # for letra in palavra_secreta:
    #     letras_acertadas.append('_')

    #usando list comprehension
    letras_acertadas = ["_" for letra in palavra_secreta]

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
        
