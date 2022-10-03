# 30/10/2022
# assert expressão [, argumentos]
# Uma verificação de robustez utilizada para realizar testes no programa
# Ele serve para verificarmos se o método é considerado True. Se não, lançará um AssertionError

import math
try:
    x = float(input('x = '))
    assert x >= 0.0
    x = math.sqrt(x)
    print('Raiz:',x)
except AssertionError:
    print(x,'é inválido')

print('Fim do Programa')