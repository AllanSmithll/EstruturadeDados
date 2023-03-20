# 20/03/2023
# Testes com o método de conversão criado
from PilhaSequencial import *

p1 = Pilha()
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(numeros)):
    p1.empilha(numeros[i])

print(p1.decToBin(p1.elemento(4)))
