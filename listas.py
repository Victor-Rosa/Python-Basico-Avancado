"""
Listas em Python funciona como vetores e matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
e também de podermos colocar QUALQUER tipo de dado

Linguagens C/java:
- Possuem tamanho e tipo de dados fixos, sem a possibilidade de mudança

Linguen Python
- Não tem tamanho fixo ou tipo fixo, nós podemos modificar a qualquer hora e adicionar qualquer tipo de dado

"""

lista_num = [10, 20, 30, 40, 50]
lista_num.insert(2, 25)
print(lista_num)

print("-" * 30)

lista_nome = list("Victor Rosa")
print(lista_nome)

print("-" * 30)

nome = "Victor"
if "V" in lista_nome:
    print("Encontrei a letra V")

print("-" * 30)

lista_num.pop(0)
print(lista_num)
print(lista_num.clear())

print("-" * 30)

time = "Flamengo é o melhor de todos"
print(time)
time = time.split()
print(time)

print("-" * 30)

time = "-".join(time)
print(time)

print("-" * 30)

frase = "Rato Roeu"
frase = frase.split()
print(frase)
frase[0], frase[1] = frase[1], frase[0]
print(frase)

print("-" * 30)

lista_num = list(range(1,5))
print(lista_num)
num1, num2, num3, num4 = lista_num
print(num1)
print(num2)
print(num3)
print(num4)

print("-" * 30)

"""----------------Shallow copy-------------"""
# Quando você modifica uma a outra TAMBÉM muda.

numeros = [1, 2, 3, 4]
print(numeros)

nova = numeros
print(nova)

nova.append(5)
print(nova)
print(numeros)

print("-" * 30)

"""-----------------Deep Copy------------------"""
# Quando você modifica uma a outra NÃO muda.

numeros = [1, 2, 3, 4]
print(numeros)

nova = numeros.copy()
print(nova)

nova.append(5)
print(nova)
print(numeros)

print("-" * 30)
