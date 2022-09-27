from Baralho import Baralho

def embaralhar():
    print('')

embaralhar()

baralho = Baralho(True)

print()
print(baralho)
print(len(baralho))

input()

print(baralho)

embaralhar()

for i in range(5):
    print(baralho.retirarCarta())

print('TOTAL DE CARTAS:', len(baralho))
