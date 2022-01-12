"""
Listas Aninhadas (Nesteds Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas arrays:
    -> Unidimensionais (Arrays/Vetores)
    -> Multidimensionais (Matrizes)

"""
# Matrizes

lista_num = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista_num)
print(type(lista_num))

print(lista_num[0][1])
print(lista_num[2][2])
print(lista_num[-1][-1])

print("-" * 50)
# List Comprehension

[[print(valor) for valor in lista] for lista in lista_num]

# Criando uma Matriz com List Comprehension

tabuleiro = [[numero for numero in range(1, 5)] for valor in range(1, 5)]
print(tabuleiro)

# Gerando um jogo da velha

velha = [['X' if numero % 2 == 0 else "O" for numero in range(1, 5)] for valor in range(1, 5)]
print(velha)