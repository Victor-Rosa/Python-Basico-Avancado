"""
Map

-> com map, fazemos um mapeamento de valores para função
-> é uma função que recebe dois parâmetros: primeiro o nome da função, segundo o iterável
-> Retorna uma Map Object
"""

import math


def area_circulo(raio):
    return math.pi * (raio ** 2)


print(area_circulo(2))
print(area_circulo(5.3))

print("-"*50)

raios = [1, 2, 5.3, 7, 9.8]

# Utlizando Map

areas = map(area_circulo, raios)
print(list(areas))
print(type(areas))

# Map com Lambda

print(list(map(lambda raio: math.pi * (raio ** 2), raios)))

converte = lambda dado: (dado[0], (9/5) * dado[1] + 32)


cidades = [('São gonçalo', 30), ('Barra', 28), ('barro vermelho', 34) ,('niteroi]', 29)]
resultado = list(map(converte, cidades))
print(resultado)