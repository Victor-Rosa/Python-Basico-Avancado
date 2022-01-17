"""
Módulos Biltion -> Módulos integrados que já vem instalado no Python

"""
# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())

from random import randint as rdi, random as rdm
print(rdi(5, 95))
print(rdm())

# Utilizando diversos imports, usamos tupla para separar melhor
from random import (
    random,
    randint,
    shuffle,
    choice)

print(random())
print(randint(50, 1000))
print(choice('Preto'))
