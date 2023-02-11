# 30/01/2023
# Teste do método criado por mim
from filaSequencialCircular import *

f1 = FilaCircular()
f2 = FilaCircular()
f3 = FilaCircular()

lista1 = [2.1, 2.5, 1.0]
lista2 = [7.2, 3.1, 9.8]

for i in range(len(lista1)):
    f1.enfileira(lista1[i])
for i in range(len(lista2)):
    f2.enfileira(lista2[i])

f1.imprime()
f2.imprime()

f3.combina(f3, f1, f2)

f3.imprime()
