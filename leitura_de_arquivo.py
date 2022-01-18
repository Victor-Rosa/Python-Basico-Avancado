"""
Leitura de Aqruivo

- Usamos a função integrada de open()
- open() -> Nós passamos um parâmetro de entrada que no caso é o caminho de documento a ser lido. Por padrão o open()
abri o arquivo apenas para leitura

mode r -> Significa modo de leitura
mode w -> Significa modo de escrita

"""

arquivo = open('texto1.txt', encoding='UTF-8')
print(arquivo)
print(type(arquivo))

ler = arquivo.read()
print(ler)