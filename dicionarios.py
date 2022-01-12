"""
OBS: Em algumas linguagens de programação dicionários são conhecidos como mapas.

* Eles são compostos por chave:valor
* Dicionários são reconhecidos por chaves: {}
* Chave e valor são separados por ":"
* Chave e valor podem ser de qualquer tipo e podem ser misturados
* São mutáveis desde que o elemento não seja uma tupla
* Em dicionário NÃO podemos ter chaves repetidas

"""

paises = {"BR": "Brasil", "EUA": "Estados Unidos", "ALE": "Alemanha", "ITA": "Itália"}
print(paises)

print("-" * 100)

paises = dict(BR='Brasil', EUA='Estados Unidos', ALE='Alemanha')
print(paises)

print("-" * 100)

# Acessando Elementos

print(paises["BR"])
print(paises["EUA"])

print("-" * 100)

# Recomendado:

print(paises.get("BR"))
print(paises.get("ALE"))

print("-" * 100)

# Encontrando Elementos

print('BR' in paises)
print('FRA' in paises)

print("Alemanha" in paises) # ele busca pela chave, não pelo valor

if 'RU' in paises:
    Russia = paises['RU']

    print("-" * 100)

# Adicionar Elementos

receita = {'jan': 100, 'fev': 200, 'mar': 350}
print(receita)

receita['abr'] = 300
print(receita)

novo_mes = {"mai": 500}

receita.update(novo_mes)
print(receita)


print("-" * 100)

# Atualizando Dados em Dicionário

receita['fev'] = 150
print(receita)

print("-" * 100)

# Remover Dados em Dicionário

# - Sempre precisamos informar a chave
# - Ao remover um elemento, o valor dele é retornado
value = receita.pop('mar')
print(value)
print(receita)

# - Desse modo o valor do elemento excluído não é retornado
del receita['jan']
print(receita)

print("-" * 100)

# Copiando um Dicionário

# - Deep Copy:
nova_receita = receita.copy()
print(receita)
print(nova_receita)

nova_receita['out'] = 700
print(nova_receita)
print(receita)

# - Shallow Copy
nova_receita2 = receita
print(nova_receita)
print(receita)

nova_receita2['ago'] = 50
print(nova_receita2)
print(receita)

print("-" * 100)


# Forma não convencional na Criação de Dicionários

usuario = {}.fromkeys(['nome', 'peso', 'altura', 'sexo'], 'desconhecido')
print(usuario)

print("-" * 100)

veja = {}.fromkeys('teste', 'valor')
print(veja)
# - 'T'/'E' não são repitidos porque dicionários não aceitam duas chaves iguais

veja2 = {}.fromkeys(range(1, 11), "None")
print(veja2)

print("-" * 100)

# Loops em Dicionário

for keys in receita:
    print(f'{keys} : {receita[keys]}')

for keys in receita.keys():
    print(keys)

for value in receita.values():
    print(value)

for keys, value in receita.items():
    print(f'Chave:{keys} | Valor:{value}')

# Métodos dentro de Dicionários

print(f'Valor Somado = {sum(receita.values())}')
print(f'Valor Máximo = {max(receita.values())}')
print(f'Valor Mínimo = {min(receita.values())}')
print(f'Tamanho do Dicionário = {len(receita)}')
