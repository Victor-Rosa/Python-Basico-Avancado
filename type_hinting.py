def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}, seja bem vindo!'


print(cumprimentar('Victor'))
print(cumprimentar(False))


def cabecalho(texto: str, alinhamento: bool = True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, '#')


print(cabecalho('Victor Rosa'))
print(cabecalho('Victor Rosa', False))
print(cabecalho('Victor Rosa', 'alou'))
