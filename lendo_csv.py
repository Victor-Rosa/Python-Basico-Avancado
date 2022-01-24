"""
Lendo arquivos CSV

* CSV : Comma Separeted Values - Valores Separados por vírgula

A linguagem python possui duas formas de trabalhar com arquivos csv :
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts
"""
from csv import reader, DictReader

# Não é o Ideal:
with open('lutadores.csv', encoding="UTF-8") as arquivo:
    dados = arquivo.read()
    dados = dados.split(",")[3:]
    print(dados)

# Ideal:
with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'Lutador: {linha[0]} | Naturalidade: {linha[1]} | Altura: {linha[2]}')

print("="*60)

# Segunda Forma Ideal:
with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"Lutador: {linha['Nome']} | Naturalidade: {linha['País']} | Altura: {linha['Altura (em cm)']}")
