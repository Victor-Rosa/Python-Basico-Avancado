"""
Escrevendo em Arquivos
- Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

- write -> para escrevermos dados em arquivo
- mode = 'w' -> para indicar que queremos escrever em um arquivo
"""

with open('novo.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Nem Toda mulher gosta de apanhar, apenas as normais.\n')
    arquivo.write('Só os profetas enxergam o óbvio. \n')    
    arquivo.write('Está é a última linha. \n')