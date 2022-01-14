"""
Any / All

- all() -> Retorna True se todos os elementos do iterável são verdadeiros ou se ele ainda estiver vazio
- any() ->

-any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""
nomes = ['Victor', 'Vitria', 'Vector', 'vitoria']


print(all(list(range(0, 5))))  # Todos os números são verdadeiros? False
print(all(list(range(1, 5))))  # Todos os números são verdadeiros? True
print(all(list()))  # Todos os números são verdadeiros? True

print(all([letra for letra in 'eio' if letra in 'aeiou']))

print("-"*50)

print(any(list(range(0, 5))))  # Todos os números são verdadeiros? False
print(any(list(range(1, 5))))  # Todos os números são verdadeiros? True
print(any(list()))  # Todos os números são verdadeiros? True

print(any([letra for letra in 'eio' if letra in 'aeiou']))

print("-"*50)

print(all([nome[0] == 'v' for nome in nomes]))
print(any([nome[0] == 'v' for nome in nomes]))
