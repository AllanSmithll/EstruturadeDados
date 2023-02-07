# 30/01/2023
# Teste do método criado por mim
from filas.filaSequencialCircular import *

p1 = FilaCircular()
p2 = FilaCircular()
p3 = FilaCircular()

p1.enfileira(2.1)
p1.enfileira(4.5)
p1.enfileira(1.0)

p2.enfileira(7.2)
p2.enfileira(3.1)
p2.enfileira(9.8)

p3.combina(p3, p2, p1)

p3.__str__()
