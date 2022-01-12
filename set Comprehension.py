"""
Set Comprehension
-> é usado o: {}
"""

lista_numeros = list(range(1,10))
print(lista_numeros)
lista_numeros.append(9)
lista_numeros.insert(0, 1)
print(lista_numeros)

lista_numeros2 = set(lista_numeros)
print(lista_numeros2)

# Fazendo em Comprehension:

lista_numeros3 = {num for num in range(1, 10)}
print(lista_numeros3)

# Em sets não existe ordem e nem valores repetidos
lista_numeros_quadrado = {num ** 2 for num in range(1, 10)}
print(lista_numeros_quadrado)

lista_numeros_quadrado2 = {num: num ** 2 for num in range(1, 10)}
print(lista_numeros_quadrado2)

nome = {letra.upper() for letra in 'Victor Rosa'}
print(nome)