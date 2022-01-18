"""
StringIo
- Para ler e escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de Leitura
    - Permissão de Escrita

StringIo -> para ler e escrever arquivos em memória.

"""

from io import StringIO

mensagem = 'Esté é uma mensagem normal'
arquivo = StringIO(mensagem)
print(arquivo.read())
arquivo.write(' Mais um texto')
arquivo.seek(0)
print(arquivo.read())