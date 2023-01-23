# 23/01/2023
from PilhaEncadeada import *

p1 = PilhaEncadeada() # PE possui start e tamanho. E o Nó possui carga e prox
p2 = PilhaEncadeada()

array1 = [1, 3, 5, 7, 9, 11, 13]
array2 = [0, 2, 4, 6, 8]

# Teste de vazio
print("Por enquanto, as pilhas estão vazias.")
print(p1.estaVazia())
print(p2.estaVazia())

# Empilhando o No(carga) na Pilha
print("\nEmpilhando os elementos nas duas Pilhas")
for i in range(len(array1)):
    p1.empilha(array1[i])
for i in range(len(array2)):
    p2.empilha(array2[i])

print(p1)
print(p2)

# Desempilhando elementos
print("\nDesempilhando vários elementos. O desempilha() faz a mesma coisa, só que apenas com o elemento start atual.")
p1.desempilha_n_elementos(2) # Desempilhou o 13 e o 11
p2.desempilha_n_elementos(1) # Desempilhou o 8

print(p1)
print(p2)

# Qual o tamanho das Pilha?
print("\nOs tamanhos das pilhas são:")
print("P1:",p1.tamanho(), "elementos.")
print("P2:",p2.tamanho(), "elementos.")

# Posição
print("\nVocê diz a posição, e o cursor percorrerá a Pilha até achar o elemento na posição referenciada.")
P1 = 1
P2 = 0

p1.elemento(P1)

print(p1.elemento(P1), f"encontrado na posição {P1} da Pilha p1.")
print(p2.elemento(P1), f"encontrado na posição {P2} da pilha p2.")

# Busca da posição do elemento

print("\nPosição do elemento 1 na Pilha p1:", p1.busca(1))
print("Posição do elemento 2 na Pilha p2:", p2.busca(2))

# Modificar elementos
print("\nModificar elementos...")
p1.modificar(3, 10)
p2.modificar(4, 20)

print("Pilha p1 após modificar():",p1)
print("Pilha p2 após modificar():",p2)

# Como saber o nó do elemento? (Se não for um método privado)
# print("\nO start das Pilhas são:")
# print("O start da Pilha é", p1.__getStart())
# print("O start da Pilha p2 é", p2.__getStart())

# Invertendo as Pilhas
print("\nInvertendo as Pilhas p1 e p2:")
p1.inverte()
p2.inverte()

print("Pilha p1 invertida:",p1)
print("Pilha p1 invertida:",p2)

# Topo e subtopo das pilhas
print("\nTopo e subtopo das pilhas:")
print(f"O topo da Pilha p1 é {p1.topo()}. Enquanto o subtopo é {p1.subTopo()}.")
print(f"O topo da Pilha p1 é {p2.topo()}. Enquanto o subtopo é {p2.subTopo()}.")

# Base das Pilhas
print("\nBase das pilhas:")
print("A base da Pilha p1 é", p1.obtemBase())
print("A base da Pilha p2 é", p2.obtemBase())

# Concatenando Pilhas
print("\nConcatenando...")
print("Primeiro, eu tenho que ter, no mínimo duas Pilhas.")
print("A Pilha p2 será usada como parâmetro a ser concatenado.")
p1.concatena(p2)

print("As pilhas p1 e p2 foram concatenadas e se transformaram nisso:", p1)

# Esvaziar para finalizar
print('\nPara terminar meus estudos de Pilha, ESVAZIAR PILHAS (Na verdade "pilha", porque concatenei a p1 com a p2)!!!')
p1.esvazia()
print("FIM!")