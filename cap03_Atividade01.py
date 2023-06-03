import random

# Diferença entre int e round... INT retira a parte decimal "trunca"...   ROUD arredonda
numero_secreto = int(93.90659198739872293)
print(numero_secreto) # 93

# Diferença entre int e round... INT retira a parte decimal "trunca"...   ROUD arredonda
numero_secreto = round(93.90659198739872293)
print(numero_secreto) # 94

# random gera um número decial entre 0 e 1, por isso multiplicamos por 100
numero_secreto = int(random.random() * 100)
print(numero_secreto)

numero_secreto = random.randrange(0,101)
print(numero_secreto)

numero_secreto = random.randint(0,11)
print(numero_secreto)

numero_secreto = random.randrange(1,10, 2)
print(numero_secreto)


