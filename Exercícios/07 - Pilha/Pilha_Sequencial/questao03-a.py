# 03/02/2023
# Testando o método concatena
from PilhaSequencial import *

# concatena()
pilha1 = Pilha()
pilha2 = Pilha()

pilha1.empilha(1.0)
pilha1.empilha(4.5)
pilha1.empilha(2.1)

pilha2.empilha(9.8)
pilha2.empilha(3.1)
pilha2.empilha(7.2)

pilha1.concatena(pilha2)

pilha1.imprime()
