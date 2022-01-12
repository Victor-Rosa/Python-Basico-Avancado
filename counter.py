"""
Módulo Collections - Counter (contador)
- High-perfomace Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário; contendo como chave: o elemento da lista passada como parâmetro; como valor: a quantidade de ocorrências
desse elemento

"""

from collections import Counter

# Utilizando o Counter
lista_numeros = [1, 2 ,3, 3, 3, 4, 5, 6, 7, 8, 9, 99, 99, 99, 99, 99, 2, 1]
resultado = Counter(lista_numeros)
print(resultado)

nome = "Idem Velle Idem Nolle"
resultado2 = Counter(nome)
print(resultado2)

lista_frase = nome.split()
resultado3 = Counter(lista_frase)
print(resultado3)