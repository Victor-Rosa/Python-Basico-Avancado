"""
O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa,
 desde que comece com asterisco

 - mas por convensão usamos: "*args"

 O parâmetro *args utilizado em função, coloca os valores extras informados como entrada em um tupla
 (tuplas são imutáveis)
"""


def soma_numeros(*args):
    total = 0
    for num in args:
        total += num
    return total



def verifica_info(*args):
    if "Victor" in args and "Rosa" in args:
        return print(f'Bem Vindo, {args[0]}')


print(soma_numeros(5, 10, 82, 10.8))
verifica_info('Victor Souza Rosa', 10, 'Rosa', True, 'Victor')

# Desempacotador

list_num = [1, 2, 3, 4, 5, 6]
print(soma_numeros(*list_num, 100))
