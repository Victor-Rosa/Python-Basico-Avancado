"""
O bloco with

O bloco with é utlizado para criar um contexto de trabalho onde os recursos utlizados são fechados após o bloco with

"""
with open('texto1.txt', encoding='UTF-8') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
