"""
Dicitionary Comprehension

o Comprehension agora usado para dicionário ao invés de listas

"""


lista_numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave: valor ** 2 for chave, valor in lista_numeros.items()}
print(quadrado)

# Adicionando chaves + valores com Comprehension
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com loja condicional

lista_numeros2 = list(range(1, 11))
resultado = {num: ('par' if num % 2 == 0 else 'impar') for num in lista_numeros2}
print(resultado)
