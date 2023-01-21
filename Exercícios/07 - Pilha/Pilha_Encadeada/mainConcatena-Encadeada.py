# 21/01/2023
from PilhaEncadeada import *

p1 = PilhaEncadeada() # PE possui start e tamanho. E o Nó possui carga e prox
p2 = PilhaEncadeada()

array1 = [1, 3, 5, 7, 9, 11, 13]
array2 = [0, 2, 4, 6, 8]

# Teste de vazio
print(p1.estaVazia())
print(p2.estaVazia())

# Empilhando o No(carga) na Pilha
for i in range(len(array1)):
    p1.empilha(array1[i])
for i in range(len(array2)):
    p2.empilha(array2[i])

print(p1)
print(p2)

p1.desempilha_algum_elemento(9)

print(p1)