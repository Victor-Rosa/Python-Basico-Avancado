"""
Zip

-> Cria um iterável (zip Object) que agrega elemento de cada um dos iteráveis passados cp,p entrada em pares
-> Os iteráveis de posições iguais, ficam dentro de uma tupla, que essa por sua vez fica dentro de uma lista
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9, 10, 11]

zip1 = zip(list1, list2)


print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))

print("-"*50)

# O zip() utiliza como parâmetro o menor tamanho em iterável

zip2 = zip(list1, list2, list3)
print(list(zip2))

print('-'*50)

zip3 = zip(list1, list2, 'abc')
print(list(zip3))

# Complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Victor', 'Maria', 'Gabriela']

resultado = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(list(zip(alunos, prova1, prova2)))
print(resultado)



