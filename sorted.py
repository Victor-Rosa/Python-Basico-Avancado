"""
Sorted

OBS: não confunda com a função sort() que já foi apresentada em Listas. o sort() só funciona em listas

-> O sorte() pode ser utilizado com qualquer iterável.
-> Ele serve para ordenar
-> O sort() modifica a própia lista já o sorted() gera momentaneamente
-> Idependente qual iterável o sorted() modifique ele sempre retornará os valores ordenados dentro de uma lista "[]"
"""

tupla_numeros = (1, 96, 20, 40, 2, 2, 7)
print(tupla_numeros)
print(sorted(tupla_numeros))
print(tupla_numeros)

print("-"*50)

# Adicionando parâmetros ao sorted()

print(sorted(tupla_numeros, reverse=True))  # Ordena do maior para o menor

# Transformando o sorted() a retorna uma tupla

print(tuple(sorted(tupla_numeros)))

# Transformando o sorted() a retorna um Set

print(set(sorted(tupla_numeros)))

# Complexos:


usuarios = [
    {"username": "Samuel", 'tweets': ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username": "Ana", 'tweets': ["Eu amo meu gato"], 'cor': "Preto", "idade": 25, 'estado civil':'casado'},
    {"username": "jeff", 'tweets': []},
    {"username": "bob", 'tweets': []},
    {"username": "diego", 'tweets': ["Eu adoro bolos", "vou sair hoje", 'Amo Pizza'], 'cor': 'Amarelo'},
    {"username": "Rodrigo", 'tweets': [], 'cor': 'Azul', 'idade': 22}
]

print(usuarios)

print(sorted(usuarios, key=lambda user: len(user['tweets'])))

print(sorted(usuarios, key=lambda user: user['username']))
