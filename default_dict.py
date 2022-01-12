"""
Módulo Collection  -  Default Dict

Default Dict -> Ao criar um dicionário utilizando-o, nó informamos um valor default, podendo utilizar um lambda para
isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe
essa chave será criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetro de entrada e retornar valores


"""

from collections import defaultdict

dicionario = defaultdict(lambda: 100)
dicionario['curso'] = 'Programacão essencial'
print(dicionario)

print(dicionario['outro'])
print(dicionario)