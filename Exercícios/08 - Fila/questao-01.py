# 30/01/2023
# Teste do método criado por mim
from filas.filaSequencialCircular import *

f1 = FilaCircular()
f2 = FilaCircular()
f3 = FilaCircular()

f1.enfileira(2.1)
f1.enfileira(4.5)
f1.enfileira(1.0)

f2.enfileira(7.2)
f2.enfileira(3.1)
f2.enfileira(9.8)

f3.combina(f3, f2, f1)

f3.imprime()
