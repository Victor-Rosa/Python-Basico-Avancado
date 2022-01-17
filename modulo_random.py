"""
Módulo Random e o que são módulos ?

- Em Python, módulos nada mais são do que outros arquivos de Python

Módulo Random -> Possui várias funções para a geração de números pseudos-aleatórios.
"""

# Ao realizar o import de todo o módulo, todas as funções, atributos classes e propiedades ficaram em memória

# Importando o módulo inteiro:
import random

print(random.random())

# Importando apenas uma função específica (FORMA RECOMENDADA):
from random import random

for i in range(0, 10):
    print(random())

# uniform() -> Gera um número pseudo-aleatório entre os valores estabelecidos
from random import uniform

for i in range(10):
    print(uniform(3, 7))

# randint() -> Gera um número inteiro pseudo-aleatório entre os valores estabelecidos
from random import randint

for i in range(10):
    print(randint(1, 61))

# choice() -> Gera um número pseudo-aleatório entre um interável
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
for i in range(10):
    print(choice(jogadas))

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9']
print(cartas)
shuffle(cartas)
print(cartas)


