"""
- Métodos de adição ou remmoção de alimentos dentro de tuplas não existem.
- Tuplas não são modificáveis, são estáticas, imutáveis
- A diferença visual de tuplas para vetores é que tuplas usam: (elemnto1, elemnto2) e não [elemento1, elemento 2]


Por que usar tuplas ?
- São mais rápidas do que listas
- Tuplas deixam seu código mais segura (tuplas são imutáveis)

"""

# Concatenação de Tuplas

tupla1 = (1, 2, 3)
print(tupla1)


tupla2 = (4, 5, 6)
print(tupla2)



print(tupla1 + tupla2)
print(tupla2)
print(tupla1)

print("-"*30)


tupla1 += tupla2
print(tupla1)

print("-"*30)

tupla3 = tupla2
print(tupla3)
print(tupla2)

tupla2 = (2,4)
print(tupla3)


