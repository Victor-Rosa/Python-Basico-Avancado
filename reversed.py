"""
Reversed

OBS: não confuna com a função reverse(), reverse() só funciona em listas

-> A função reversed() funciona com qualquer lista
-> Sua função é inverter o iterável

"""

tupla_numeros = tuple(range(0, 10))
print(tupla_numeros)

print("-"*50)

print(list(reversed(tupla_numeros)))
print(tuple(reversed(tupla_numeros)))
print(set(reversed(tupla_numeros)))

