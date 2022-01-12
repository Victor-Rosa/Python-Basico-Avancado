"""
Loop for

Loop -> Estrutura de repetição

a função range()
"""
bicicletas = ["nixon", "adidas", "nike"]
for i in bicicletas:
    print(i)

numbers = range(0, 20)
for num in numbers:
    print(num)

print(numbers)

name = "Victor Rosa"
for letra in name:
    print(letra)

print(name[::-1])

print(len(name))

"""
------ Enumerate:
((0, V), (1, i), (2, c)...) 
-> Ele gera uma lista de tuplas que ordena cada palavra de uma String e um índice.
"""
for indice, letra in enumerate(name):
    print(name[indice])

for tupla in enumerate(name):
    print(tupla)

for letra in name:
    print(letra, end='')

print(name*3)

for num in range(10, 0, -2):
    print(num)
numbers = list(range(0, 20))
print(numbers)