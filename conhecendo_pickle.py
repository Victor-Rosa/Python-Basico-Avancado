"""
 Pickle

A função do pickle:
- Objeto Python -> Binarização
- Binarização -> Objeto Python

#OBS: O módulo pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar
com arquivos pickle vindos de outras pessoas que você não conheça ou de fontes desconhecidas

"""

import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def get_nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.get_nome} está miando')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.get_nome} está latindo')


felix = Gato('felix')
pluto = Cachorro('pluto')

# Fazendo a escrita em arquivos pickle
with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)

# Fazendo a leitura em arquivos pickle
with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se: {gato.get_nome}')
    print(f'O gato chama-se: {cachorro.get_nome}')
    cachorro.late()
    gato.mia()

