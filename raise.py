"""
Levantando os própios erros com raise

OBS: O raise não é uma função, é uma palavra reservada, assim como def ou qualquer outra em python
raise -> lança exceções
-> O raise, assim como o return, finaliza a função, ou seja nada após ele é executado, o programa para nele
"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa aser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto: {texto}, será impresso na cor: {cor}')


colore('geek', 'vermelho')