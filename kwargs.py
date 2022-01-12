"""
Parecido com o *args

- Diferente do *args que coloca os valores em uma tupla o **kwargs exige que utilizamos parâmetros nomeados
e transforma esses parâmetros extras em um dicionário

-> Os valores não são obrigatórios
"""


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'Nome: {pessoa.title()} | Cor preferida: {cor}')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você Passou no Teste!'
    elif 'geek' in kwargs:
        return 'Você meio que passou no Teste.'
    return 'Você não passou no teste...'


def minha_funcao(nome, idade, *args, solteiro=True, **kwargs):
    print(f'Nome:{nome}|idade{idade}')
    print(args)
    if solteiro:
        print(f'Estado Civil:{solteiro}')
    else:
        print('Estado Civil:casado')
    print(kwargs)



cores_favoritas(MARCOS='vermelho', Julia='Rosa', antonio='Azul', victor='Preto Fosco')

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Especial'))

print(minha_funcao('Victor', 22))
print(minha_funcao('Lucas', 28, 21991665735, False, cep=24461380))
print(minha_funcao('Rafael', 99, Java=False, cep=24461380, tel='2199166535'))

# Desempacotar com **Kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'VICTOR', 'sobrenome': 'Rosa'}
print(mostra_nomes(**nomes))


def soma_num(num1, num2, num3):
    return (num1+num2+num3)


lista = [1, 2, 3]
tupla = (1, 8, 3)
conjunto = {1, 10, 3}

print(soma_num(*lista))
print(soma_num(*tupla))
print(soma_num(*conjunto))
