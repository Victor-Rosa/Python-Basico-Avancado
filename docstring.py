"""
Documentando função com Docstring

OBS: podemos ter acesso á documentação de uma função em Python usando a propiedade: __doc__
"""


def diz_oi():
    """Uma função que retorna: oi"""
    return "OI"

string = diz_oi()
print(string)
print(diz_oi.__doc__)
