"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas dentro das nossas list comprehension
"""

lista_numeros = list(range(1, 7))

numeros_pares = [numero%2==0 for numero in lista_numeros]
print(numeros_pares)

numeros_pares2 = [numero for numero in lista_numeros if numero % 2 == 0]

numeros_impares = [numero for numero in lista_numeros if numero % 2 != 0]

print(numeros_pares2)
print(numeros_impares)

# Qualquer número par módulo de 2 é 0 e 0 em python é = False.  not False = True
numeros_pares3 = [numero for numero in lista_numeros if not numero % 2]
numeros_impares2 = [numero for numero in lista_numeros if numero % 2]
print(numeros_pares3)
print(numeros_impares2)

resultado = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in lista_numeros]
print(resultado)
