

def gg():
    # def nome_funcao(), cria uma função, basta identar o código para inserir ações
    print("*" * 28)
    print(" Jogo da forca ".center(28,"-"))
    print("*" * 28)
    
    palavra_secreta = 'banana'

    morreu = False
    acertou = False

    # enquanto não morreu E não acertou 
    # enquanto não False
    # enquanto (True)

    while(not morreu and not acertou):
        tentativa = input('Qual a letra? ').strip()

        index = 0
        for letra in palavra_secreta:
            if (tentativa.upper() ==  letra.upper()):
                print(f'Encontrei a letra {letra} na posição {index}')
            index += 1
        
        print('GG forca')

    print('\nObrigado por participar!\n')

if (__name__ == "__main__"):
    gg()
        
