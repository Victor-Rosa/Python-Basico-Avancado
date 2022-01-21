"""
POO - Atributos

Atributos: Representam as características do objeto. Ou seja, pelos os atributos nós conseguimos representar
computacionalmente os estados de um objeto

Em Python dividimos os atributos em 3:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

# Atributos de Instância são atributos declarados dentro de um método construtor

# Em python por conversão ficou estabelecido que todos os atributo de uma classe é público. Casso queria tornar um atri
buto em privado, basta colocar: "__" no ínício do seu nome
"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos x Privados

# Atributo Privado:
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem python não vai impedir que façamos acesso aos
# atributos sinalizados como privados fora da classe

# Exemplo:

user = Acesso('user@gmail.com', '12345')
print(user.email)
# print(user.__senha) # AtributeError
print(user._Acesso__senha)  # Name Mangling

user.mostra_email()
user.mostra_senha()


# Atriibutos de Classe -> são atributos que são declarados direatamente na classe, ou seja, fora do construtor.
# Geralmente já incializamos um valor, e este valor é compartilhado entre todas as instâncias da classe.
# Ou seja, ao invés de cada instância da classe ter seus própios valores como é o caso dos atributos de instância,
# com os atributos de classe ttodas as intâncias terão o mesmo valor para este atributo


# Refatorar a classe Produto


class Produto:

    # Atributos de Classe:
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


p1 = Produto('PS4', 'Video-game', 2300)
p2 = Produto('PS5', 'Video-game', 6300)
p3 = Produto('Xbox-s', 'Video-game', 4300)

print(p1.imposto)
print(p2.imposto)
print(p3.imposto)

print(p1.valor)
print(p2.valor)
print(p3.valor)

print(p1.id)
print(p2.id)
print(p3.id)

# Atributos Dinâmicos -> um atributo de instância que pode ser criado em tempo de execução.
# OBS: o atributo dinâmico será exclusivo da instância que o criou

p4 = Produto('Arroz', 'Mercearia', 5.99)
p4.peso = '5kg'  # Note que a classe produto não existe o atributo peso
print(f'Produto: {p4.nome}| Preço: {p4.valor} | Peso: {p4.peso}')
print(f'Produto: {p2.nome}| Preço: {p2.valor} |')
print(f'Produto: {p1.nome}| Preço: {p1.valor} |')

# Deletando Atributos
print(p4.__dict__)
print(p2.__dict__)
print(p1.__dict__)

del p4.peso
del p2.descricao
del p1.valor

print(p4.__dict__)
print(p2.__dict__)
print(p1.__dict__)