"""
Escrevendo em CSV

reader() (leitor), writer() (escritor)

* w -> Para criar um arquivo novo e escrever nele
* a -> para escrever em um arquivo já existente

- write() ->  Gera um objeto para que possamos escrever em um arquivo CSV
- writerow() -> Utilizamos para escrever cada linha. Esse método recebe uma lista.

"""
from csv import writer, DictWriter
print('Primeiro')
if arquivo := input("Quer criar um arquivo novo (sim/nao): ") != 'nao':
    with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
        escritor_csv = writer(arquivo)
        filme = None
        escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
        while filme != 'sair':
            filme = input('Nome do Filme: ')
            if filme != 'sair':
                genero = input('Gênero do Filme: ')
                duracao = input('Duração do Filme (em minutos): ')
                escritor_csv.writerow([filme, genero, duracao])
else:
    with open('filmes.csv', 'a', encoding='utf-8') as arquivo:
        escritor_csv = writer(arquivo)
        filme = None
        while filme != 'sair':
            filme = input('Nome do Filme: ')
            if filme != 'sair':
                genero = input('Gênero do Filme: ')
                duracao = input('Duração do Filme (em minutos): ')
                escritor_csv.writerow([filme, genero, duracao])

print('Segundo')
print("="*60)
# Utilizando DictWriter:
# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.
with open('filmes2.csv', 'w', encoding='utf-8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames= cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Nome do Filme: ')
        if filme != 'sair':
            genero = input('Gênero do Filme: ')
            duracao = input('Duração do Filme (em minutos): ')
            escritor_csv.writerow({"Título": filme,"Gênero": genero, "Duração": duracao})




