"""
Módulo Collections: Ordered Dict

OrderedDict -> é um dicionário que nos garante a ordem de inserção dos elementos
"""

from collections import OrderedDict
# Dicionários Comuns
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dicionario2 = {'c': 3, 'b': 2, 'a': 1, 'd': 4}
print(dicionario == dicionario2) # True

# Ordered Dict
dicionario3 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
dicionario4 = OrderedDict({'c': 3, 'b': 2, 'a': 1, 'd': 4})
print(dicionario3 == dicionario4) # False
