"""
- No Python os Conjuntos são chamados de Sets

- Sets NÃO possuem valores duplicados
- Sets NÃO possuem valores ordenados
- Elementos NÃO são acessados via índice; conjuntos NÃO são indexados

* Conjuntos são bons para se utulzar quando precisamos armazenar elementos mas ao nos importamos com a orndenação deles.
 Quando não precisamos se preocupar com chaves, valores e itens duplicados

* Os Sets são referenciados por chaves: "{}"

Diferenças de Sets para Dicionários:
    - Dicionários possuem chave:valor
    - Sets só possuem valores

* Podemos colocar tipos de dados misturados em Sets
"""

# Definindo um Conjunto

test_sets = set({1, 2, 3, 4, 5, 5, 2, 7, 3})
print(test_sets)

test_sets2 = {1, 2, 3, 4, 5, 7, 6, 1}
print(test_sets2)
print(type(test_sets2))

test_sets3 = set("Victor Rosa")
print(test_sets3)

test_sets4 = set({1, "VICTOR", 1.84, "rOSA", 156, "S"})
print(test_sets4)

print("-" * 50)
# Adiconado um Elemento

test_sets5 = {1, 2, 4}
test_sets5.add(78)
print(test_sets5)

print("-" * 50)

# Removendo um Elemento

test_sets5.remove(2)
print(test_sets5)

print("-" * 50)

# Formando um novo Set

# Deep Copy

print(test_sets5)

test_sets6 = test_sets5.copy()
print(test_sets6)

test_sets6.add(89)
print(test_sets6)
print(test_sets5)

# Shallow Copy

print(test_sets5)

test_sets7 = test_sets5
test_sets7.add(1999)
print(test_sets5)
print(test_sets7)

print("-" * 50)

# Métodos Matemáticos de Conjuntos


estudante_java = {"Patrícia", "Lohandro", "Michael", 'Victor', 'Alexandra'}
estudante_python = {'Victor', 'Marcela', 'Antônio', 'Michael'}
print(f'{estudante_python} Qtd Alunos: {len(estudante_python)}')
print(f'{estudante_java} Qtd Alunos: {len(estudante_java)}')

# Utilizando Union:
estudante_total = estudante_java.union(estudante_python)
print(f'{estudante_total} Qtd Alunos: {len(estudante_total)}')

# Utilizando Pipe: "|"
estudante_total2 = estudante_java | estudante_python
print(f'{estudante_total} Qtd Alunos: {len(estudante_total)}')

# Formando um Conjunto com alunos que estão em ambos os cursos

# Utilizando Intersection
estudante_ambos2 = estudante_java.intersection(estudante_python)
print(f'{estudante_ambos2} Qtd Alunos: {len(estudante_ambos2)}')

# Utilizando o "&"
estudante_ambos = estudante_java & estudante_python
print(f'{estudante_ambos} Qtd Alunos: {len(estudante_ambos)}')


# Gerar um conjunto de estudantes que não estão no outro curso

estudante_apenas_python = estudante_java.difference(estudante_python)
estudante_apenas_java = estudante_python.difference(estudante_java)
print(f'Python: {estudante_apenas_python} Qtd Alunos: {len(estudante_apenas_python)}')
print(f'Java: {estudante_apenas_java} Qtd Alunos: {len(estudante_apenas_java)}')

print("-" * 50)
