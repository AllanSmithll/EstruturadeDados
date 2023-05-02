# 30/01/2023
# Testes do método criado por mim -> ABANDONADO
from filaSequencialCircular import *

f1 = FilaCircular(3)
f2 = FilaCircular(3)
f3 = FilaCircular(6)

lista1 = [2.1, 4.5, 1.0]
lista2 = [7.2, 3.1, 9.8]

for i in range(len(lista1)):
    f1.enfileira(lista1[i])
for i in range(len(lista2)):
    f2.enfileira(lista2[i])

print(f1.imprime())
print(f2.imprime())
print(f3.imprime())

# Letra A
FilaCircular.combina(f3, f1, f2)

print(f3.imprime())
