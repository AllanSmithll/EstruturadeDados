# 25/01/2023
# Testando o método inverte feito por mim
from PilhaSequencial import *

if __name__ == '__main__':
    p1 = Pilha()
    p1.empilha(10)
    p1.empilha(20)
    p1.empilha(30)
    p1.empilha(40)
    p1.empilha(50)
    p1.empilha(60)
    p1.imprime()
    p1.inverte()
    p1.imprime()
    print(p1.inverte())