"""
List Comprehension

-> Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável
"""


def dobrado(number):
    return number * number


lista_numeros = list(range(1, 6))
print(lista_numeros)

resultado = [numero * 10 for numero in lista_numeros]
print(resultado)

resultado2 = [numero / 2 for numero in lista_numeros]
print(resultado2)

resultado3 = [dobrado(numero) for numero in lista_numeros]
print(resultado3)

nome = 'victor rosa'
resultado4 = [letra.upper() for letra in nome]
print(resultado4)

lista_amigos = ['João', 'Maria', 'rodrigo']
resultado5 = [amigo[0].upper() for amigo in lista_amigos]
print(resultado5)

print([str(numero) for numero in [1, 2, 3, 4]])
