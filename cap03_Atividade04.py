import aforca
import adivinhe
from os import system
system('cls')

def escolha_jogo():
    print('***************************************')
    print('-------- Escolha seu Game! ------------')
    print('***************************************')

    print('\n(1) Forca \n(2) Adivinhe o número')
    jogo = int(input('Qual vai ser o game? '))

    if (jogo == 1):
        aforca.gg()
    elif (jogo == 2):
        adivinhe.gg()

if(__name__ == "__main__"):
    escolha_jogo()
