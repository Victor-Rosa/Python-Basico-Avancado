"""
Filter

-> serve para filtrar dados de uma determinada coleção
-> Recebe dois parâmetros, uma função e um interável e retorna um objeto filtrando apenas os elementos de acordo com
a função passada
"""
import statistics


valores = 1, 2, 3, 4, 5, 6
print(valores)

media = (sum(valores)/len(valores))
print(media)

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media2 = statistics.mean(dados)
print(f'Media: {media2}')

resultado = filter(lambda value: value > media2, dados)
print(list(resultado))
# Obs após ser utilizado os dados do filter eles são excluídos da memória
print(f'Imprimindo a resposta novamente: {list(resultado)}')

paises = ["", "Argentina", "Equador", "Bolivia", "", " ", "Alemanha", "Brasil"]
resultado2 = filter(lambda pais: pais != ' ' and pais != '', paises)
print(list(resultado2))

usuarios = [
    {"username": "Samuel", 'tweets': ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username": "Ana", 'tweets': ["Eu amo meu gato"]},
    {"username": "jeff", 'tweets': []},
    {"username": "bob", 'tweets': []},
    {"username": "diego", 'tweets': ["Eu adoro bolos", "vou sair hoje"]},
    {"username": "Rodrigo", 'tweets': []}
]

inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))
print(inativos)

inativos2 = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos2)

nomes = ['Ana', 'Livia', 'Beatriz']
estrutoras = list(map(lambda nome: f'A sua estrutora é {nome}', filter(lambda nome: len(nome) > 3, nomes)))
print(estrutoras)
