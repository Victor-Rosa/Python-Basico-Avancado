"""
POO - Herança Múltipla

Herança Múltipla -> nada mais é do que a possibilidade de uma classe herdar de mútiplas classes, fazendo com que a
classe filha herde todos os atributos e métodos de todas as classes herdadas

"""


# Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3(Base1, Base2):
    pass


# Mulriderivação Indireta

class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base5):  # Está herdando a Base4 de tabela
    pass


class Base7(Base6):  # Está herdendo a Base4 e Base5 de tabela
    pass


# Exemplo Real
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Olá eu sou o: {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está Nadando'

    def cumprimentar(self):
        return f'Oi eu sou o {self._Animal__nome} do mar'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está Andando'

    def cumprimentar(self):
        return f'Oi eu sou o {self._Animal__nome} da Terra'


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.cumprimentar())
print(baleia.nadar())

cachorro = Terrestre('Otto')
print(cachorro.cumprimentar())
print(cachorro.andar())

pinguim = Pinguim('Happy Feet')
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.cumprimentar())

# Descobrir se um objeto e instância de outro

print(f'Cachorro é instância de Pinguim: {isinstance(cachorro, Pinguim)}')
print(f'Cachorro é instância de Aquatico: {isinstance(cachorro, Aquatico)}')
print(f'Cachorro é instância de Terrestre: {isinstance(cachorro, Terrestre)}')
print(f'Cachorro é instância de object: {isinstance(cachorro, object)}')
