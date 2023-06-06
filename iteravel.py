
## tudo que eu posso iterar
## iterar : fatiamento
## str -> iteravel

texto = "    Curso de Python II WEB    "

#fatiamento
print(texto[6])
print(texto[:6])
print(texto[0:6+1])
print(len(texto))
print(texto[0:len(texto):2])

#metodos de string
texto_sem_espacos = texto.strip()
print(texto_sem_espacos)

#UPPER, LOWER, SPLIT
print(texto_sem_espacos.upper())
print(texto_sem_espacos.lower())
print(texto_sem_espacos.split())

# PELACE
print(texto_sem_espacos.replace("II", "I"))


#CENTER
print((' '+texto_sem_espacos+' ').center(30,"*"))