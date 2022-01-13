"""
Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente lambdas, na verdade são funções anônimas.

"""


def funcao(x):
    return 3 * x + 1


print(funcao(5))


# Utlizando Lambdas
lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1
print(calc(5))

# strip() -> serve para tirar os espaços no final ou começo de uma string
nome_completo = lambda nome, sobrenome: nome.strip().title() + '' + sobrenome.strip().title()
print(nome_completo(' victor', ' rosa'))

autores = ['Fiodor Doistoévski', 'G.K Chersterton', 'C.S Lewis', 'Jordan Peterson', 'Olavo de Carvalho']

print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Deifinindo a funcao

def geradora_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(2))
print(teste(1))
print(teste(0))
