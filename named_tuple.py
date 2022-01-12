"""
Módulo Collections - Named TUple

Named Tuple -> São tuplas diferenciadas onde especififcamos um nome para a mesma e também parâmetros
"""
from collections import namedtuple

# Declaraçao Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando Named Tuple

dog1 = cachorro(idade=4, raca='Bulldog', nome='Otto')
print(dog1)
print(f'idade: {dog1[0]}')
print(f'raca: {dog1.raca}')
