"""
Bloco try/except

Utilizamos o bloco  try (tente fazer isso)/except (caso não consiga, faça isso) para tratar erros que podem ocorrer
no nosso código. Previnindo assi que o prorama pare de funcionar e o usuário receba a mensagens de erro inesperadas

************* TODA ENTRADA DEVE SER TRATADA **********************

- Escopo:
    try:
        //EXECUÇÃO PROBLEMÁTICA
    except:
        //O QUE DEVE SER FEITO EM CASO DE PROBLEMA

Else -> é executado somente se não ocorrer o erro
Finally -> é sempre executado. Independente se der erro ou não / ele é usado para fechar ou deslocar recursos

- Uma boa prática é executar o tratamento de erro dentro da sua função e não no escopo global, você é responsável pelas
entradas que você recebe da sua função criada
"""

# Tratando Erro genérico
try:
    geek()
except:
    print('Você executou uma ação que não existe')

    print("-" * 50)

# Tratando Erro específico
try:
    geek()
except NameError:
    print('Você executou uma função que não existe')

print("-" * 50)

# Com detalhes do Erro:
try:
    len(5)
except TypeError as err:
    print(f' A aplicação gerou o seguinte erro: {err}')

print("-" * 50)

# Podemos efetuar diversos tratamentos de erros de uma vez
try:
    len(5)
except NameError as erra:
    print(f'Deu NameError {erra}')
except TypeError as errb:
    print(f'Deu TyperError {errb}')
except:
    print('Deu um erro diferente')

print("-" * 50)


# Tratamento de Erro em funções


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as err:
        print(f'Essa chave: {err}, não existe nesse dicionário: {dicionario}')
        return None


nome_idade = {'Victor': 22, 'Daniel': 20, 'Livia': 20}
print(pega_valor(nome_idade, 'juliana'))

print("-" * 50)

# Utilizando o Else
numero = 0
try:
    numero = int(input('Informe um Número: '))
except ValueError as err:
    print(f'{err} * Por favor Digite um número *')
else:
    print(f'Você digitou: {numero}')

    print("-" * 50)

# Utilizando o Finally

try:
    numero = int(input('Informe um Número: '))
except ValueError as err:
    print(f'{err} * Por favor Digite um número *')
else:
    print(f'Você digitou: {numero}')
finally:
    print('Executando o finally')

print("="*50)

# Mais Complexo


def dividir(num1, num2):
    try:
        result = int(num1) / int(num2)
        return result
    except (ValueError, ZeroDivisionError) as err:
        return f'Error: {err}, Por favor digite um número e maior que zero.'
    except NameError as errb:
        return f'Error {errb}'
    else:
        print(f'A divisão entre {num1} e {num2}: {result}')



num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
print(dividir(num1, num2))

