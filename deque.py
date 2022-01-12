"""
Módulo Collections - Deque

Deque -> uma lista de alta performace

"""
from collections import deque

# Criando Deques
deq = deque('Geek')
print(deq)

# Adicionando Elementos
deq.append("Rosa")
print(deq)

deq.appendleft('Victor')
print(deq)

# Removendo Elementos

deq.pop()
print(deq)

deq.popleft()
print(deq)