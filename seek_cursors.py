"""
Seek e Cursors

- seek() -> é utlizado para movimentar o cursor pelo arquivo, ela recebe um parâmetro que indica onde queremos
 colocar o cursor
- readline() -> le linha por linha do arquivo
- closed() -> verifica se o arquivo está fechado
- read() -> com a função read podemos limitar quantos caracteres serão lidos
"""

arquivo = open('texto1.txt', encoding='UTF-8')

print(arquivo.read())
arquivo.seek(10) #
print(arquivo.read())
print(arquivo.readline(0))
print(arquivo.closed)

arquivo.close()
print(arquivo.closed)
