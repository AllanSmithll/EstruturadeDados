# 20/03/2023
# Teste do método criado
from PilhaSequencial import *

p1 = Pilha()
frase = "Allan é gostoso"
inicio = 0
fim = 1

for i in frase:
    p1.empilha(frase[inicio:fim])
    inicio += 1
    fim += 1

p1.inverte()
p1.imprime()
