"""
POO - Objetos

Objetos -> são instâncias da classe. Objetos e Instâncias são a mesma coisa
"""


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def hellou(self):
        print('Hello World')


class ContaCorrente:

    def __init__(self, cliente, limite, saldo):
        self.__cliente = cliente
        self.__limite = limite
        self.__saldo = saldo

    def exibi_cliente(self):
        print(f' O cliente é {self.__cliente._Cliente__nome}')


cl1 = Cliente("Victor", "15721964738")
user = ContaCorrente(cl1, 4700, 280)
print(user.exibi_cliente())
user._ContaCorrente__cliente.hellou()