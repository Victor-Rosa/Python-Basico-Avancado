"""
POO - Metodos

Metodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu
sistema.

Dividimos os Métodos em 2:
    - Métodos de Instância
    - Métodos de Classe

"""
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, voltagem, cor, luminosidade, ):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 1234

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    # Atributos de Classe:
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor * Produto.imposto
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    contador = 0

    @classmethod
    def conta_usario(cls):  # cls -> a classe
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s)  no sistema')

    @staticmethod
    def definicao():
        return 'Urx89'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
        self.__sobrenome = sobrenome
        Usuario.contador = self.__id

    def nome_completo(self):
        return self.__nome.title() + " " + self.__sobrenome.title()

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return f' Usuario Gerado: {self.__email.split("@")[0]}'



p1 = Produto('PS4', 'Video-game', 2300)
print(p1.desconto(50))

user1 = Usuario('Victor', 'Rosa', 'victor@email.com', '1012')
print(user1.nome_completo())

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Digite a senha: ')
confirma_senha = input('Confirma a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print(f'Usuário: {user.nome_completo()} criado com sucesso')
else:
    print('As senhas digitadas não são iguais')

senha = input('Informe a senha para o acesso: ')

if user.checa_senha(senha):
    print('Permissão Concedida')
else:
    print('Permissão Negada')

print(f'Senha Criptografada: {user._Usuario__senha}')


print(Usuario.conta_usario())
print(Usuario.definicao())
userX = Usuario('victor', 'rosa', 'victor@gmail.com', '12345')
print(userX._Usuario__gera_usuario())
print(userX.__gera_usuario())