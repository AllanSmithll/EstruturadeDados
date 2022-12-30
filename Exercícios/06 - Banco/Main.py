from Conta import Conta
from Banco import *

try:
    bco = Banco()
    bco.addConta(123, 'Alex')
    bco.addConta(456, 'Clodoaldo')
    bco.addConta(457, 'Yago')
    bco.addConta(458, 'Márcio')
    bco.addConta(120, 'Caio')
    bco.addConta(121, 'Felipe')
    bco.addConta(12, 'Allan')
    
    bco.sacar(456, 10.00)

    # Meu teste do método depositar
    bco.depositar(458, 100.00)

    bco.acessarConta(458)
    

except OperacaoInvalidaException as oie:
    print(oie)

print(bco)

