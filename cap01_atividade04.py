#Cumprindo a tadição em Python
print('Olá Mundo')

#podemos usar o comando format para concatenar texto
#print('Olá {}' . format(input('Qual o seu nome? ') + '!')) # metodo format da classe str
# print(f'Olá :{input("Qual seu nome")} !')  # f-string
curso = "Python Web"
unidade = 'TAU'
cidade = 'Taubaté'

texto01 = 'Curso {} no Senac {} na cidade de {}'.format(curso,unidade,cidade)
texto01 = 'Curso {c} no Senac {u} na cidade de {cid}'.format(cid=cidade,u=unidade,c=curso)
texto02 = f'Curso {curso} no Senac {unidade} na cidade de {cidade}'

print(texto01)
print(texto02)

# é possível colocar dois ou mais textos separados por vígula
print('Seja bem-vindo a aula de' + 'Python II')
print('Seja bem-vindo a aula de', 'Python II')

texto03 = '''
kljsdjfla
ladjsfla
klglkajflajsdlçfka
'''
print(texto03)

x = input("digite algo:  ")
x = float(x)
print(type(x))





