"""
POO - Herança

A ideia dela é de reaproveitar código e estender nossas classes

OBS: A partir de um classe existente nós extendemos outra classe que passa a herdar atributos e métodos da classe
herdada

- Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    - Super Classe
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Classe Genérica

- Quando uma classe herda de outra classe, ela é chamada:
    - Classe Filha
    - Sub Classe
    - Classe Específica
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma comum
        self.__matricula = matricula

    def nome_completo(self):
        return  f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'


primeiro_cliente = Cliente('Victor', 'Rosa', '15721964758', 2500)
print(primeiro_cliente.nome_completo())

primeiro_funcionario = Funcionario('Rafael', 'Santos', '25975974658', 89658)
print(primeiro_funcionario.nome_completo())

print(primeiro_funcionario.__dict__)
print(primeiro_cliente.__dict__)