"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão

variavel := expressão
"""

nome1 = 'victor rosa'
print(nome1)

print(nome2 := 'victor rosa')

# Python 3.7
cesta = []
fruta = input('Informe uma fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)

# Python 3.8
cesta2 = []
while (fruta := input('Informe uma fruta')) != 'jaca:':
    cesta2.append(fruta)