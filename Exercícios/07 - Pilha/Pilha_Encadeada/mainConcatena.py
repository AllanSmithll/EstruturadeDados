from PilhaEncadeada import *

p1 = Pilha()
p2 = Pilha()

array1 = [1, 3, 5, 7, 9, 11, 13]
array2 = [2, 4, 6, 8]

for value in array1:
    p1.empilha(value)

for value in array2:
    p2.empilha(value)

print('P1:', p1)
print('P2:', p2)

p1.concatena(p2)

print('P1 com P2:', p1)