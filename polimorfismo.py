"""
POO - Polimorfismo

poli -> Muitas
Morfis -> Forma

Quando a gente reimplementa um método presente na classe pai em classes filhas estamos realizando uma sobrescrita de
 método (Overriding).

 O Overriding é a melhor representação do polimorfismo
"""


class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau miau')


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)


felix = Gato('felix')
pluto = Cachorro('pluto')
mickey = Rato('Mickey')

felix.falar()
felix.comer()

pluto.falar()
pluto.comer()

mickey.falar()
mickey.comer()
