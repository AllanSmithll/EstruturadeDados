# 03/02/2023
# Notação Polonesa Reversa
from PilhaSequencial import *
import string

pilha = Pilha()
expressao = 'A*(B+C)/D'
saida = ''

while True:
    for i in range(len(expressao)):
        if expressao[i] == string.ascii_letters:
            saida += expressao[i]
    break

print(saida)
