from Baralho import Baralho
from Carta import Carta

c = Carta('2','espada','vermelho')
c.valor = 'rei'
print(c)

input()

def embaralhar():
    print('função embaralhar()')

embaralhar()


baralho = Baralho(True)
#baralho.embaralhar()

#for i in range(53):
#    print(baralho.retirarCarta())

while(baralho.temCarta()):
    carta = baralho.retirarCarta()
    print(carta)

print('Não há mais cartas a serem retiradas')
print('Total de cartas no baralho:', len(baralho))

baralho.receberCarta(carta)
baralho.receberCarta(carta)
print('Total de cartas no baralho:', len(baralho))
print(baralho)

baralho2 = Baralho()
for i in range(42):
    baralho2.retirarCarta()
print('Baralho 2\n')
print(baralho2)

print('fazer o baralho 1 receber as cartas do 2')
baralho.juntarBaralho(baralho2)
print(baralho)
print(len(baralho))
print(len(baralho2))
input()
alunos = {10:'Lucas',11: 'Luis',12:'Yago' }
baralho.container.append(alunos)
print(baralho)



'''

print()

print(len(baralho))

input()

print(baralho)

embaralhar()
'''