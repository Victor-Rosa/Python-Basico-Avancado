"""
POO - Propiedades

Em Java ao declararmos atributos provados nas classes, costumamos a criar métodos públicos para manipulação desses
atributos. Esses métodos são chamados de getters e setters;

- Getters: retorna o valor do atributo
- Setters: alteram o valor do atributo
"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente: {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def soma_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Victor', 180, 4700)
conta2 = Conta('Rafael', 8000, 20000)

print(conta1.extrato())
print(conta2.extrato())

soma_contas1 = conta1._Conta__saldo + conta2._Conta__saldo
print(f'A soma do saldo das duas contas é: {soma_contas1}')  # Forma Errada

soma_contas2 = conta1.saldo + conta2.saldo
print(f'A soma do saldo das duas contas é: {soma_contas1}')  # Forma Certa

print(conta1.limite)
conta1.limite = 6832
print(conta1.limite)

print(conta1.soma_total)
