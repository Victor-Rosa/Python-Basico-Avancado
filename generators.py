"""
Generators

e a list comprehension mas com tupla (tupla comprehension == generators)

-> o Generator ocupa menos recurso em memória (mais eficiente)
-> Enquanto o List comprehension retorna uma lista; o generators retorna um objeto
"""
from sys import getsizeof

nomes = ['Victor', 'Vitria', 'Vector', 'vitoria']


print(any(nome[0] == 'V' for nome in nomes))
print(all(nome[0] == 'V' for nome in nomes))

print("-"*50)

# Perceba que não usamos "[]" para poder fazer o comprehension

# List Comprehension
print(any([nome[0] == 'V' for nome in nomes]))
print(type(any([nome[0] == 'V' for nome in nomes])))

# Generators
print(any(nome[0] == 'V' for nome in nomes))
print(type(any([nome[0] == 'V' for nome in nomes])))

print("-"*50)

# getsizeof -> retorna a quantidade de bytes em memória do elemento passado como parâmetro

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof(([x * 10 for x in range(1000)]))

# Gerando uma lista de números com List Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com List Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com List Comprehension
generator = getsizeof((x * 10 for x in range(1000)))

print(f'List Comprehension: {list_comp} byte')
print(f'Set Comprehension: {set_comp} byte')
print(f'Dictionary: {dic_comp} byte')
print(f'Generator: {generator} byte')




