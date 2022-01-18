"""
Sistema de Arquivos - Manipulação


"""
import os

# Descobrindo se um arquivo existe:

# Arquivo
print(os.path.exists('university.txt'))
# Diretório
print(os.path.exists('geek'))
print(os.path.exists('outro'))

# Criando Arquivos
open('arquivos-teste.txt', 'w').close()
open('arquivos-teste2.txt', 'a').close()

# Criando Diretórios
# os.mkdir('templates')
# os.makedirs('templates2/geek2/university2')

# Renomear Arquivos
# os.rename('templates2', 'geek-template')

# Deletar Arquivos
# os.remove('texto-teste.txt')

# Deletando Diretórios Vazios
# os.removedirs('templates')

# Removendo Árvore de Diretórios

# for arquivo in os.scandir('geek-template'):
#    if arquivo.is_file():
#        os.removedirs(arquivo.path)

from send2trash import send2trash

send2trash('arquivos-teste.txt')
