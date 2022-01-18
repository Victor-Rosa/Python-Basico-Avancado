"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobscreve caso o arquivo já exista
x -> Abre para escrita - somente se o arquivo não existir
a -> Abre para escrita adicionando o conteúdo Sempre ao final do arquivo - Se o arquivo não existir será criado
+ -> Abre para o modo de atualização - Leitura e Escrita
"""
try:
    with open('university.txt', 'a+', encoding='UTF-8') as arquivo:
        arquivo.seek(0)
        arquivo.write('Novo topo\n')
        arquivo.write('Novo segundo\n')
        arquivo.write('Novo Terceiro\n')
except FileExistsError:
    print('Este arquivo já existi')