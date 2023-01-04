from PilhaSequencial import *

numeros = [4,5,6,90,56,31,42,57] # Lista a ser empilhada

pilha = Pilha() # Crio um objeto pilha para usar
for n in numeros:
    pilha.empilha(n) # Empilho cada elemento da lista "numeros"

print('Array: ',numeros)  # Imprimo o array inicial
print('Pilha: ', pilha) # A pilha depois que utilizei do método "empilha()"

esta_vazia = pilha.estaVazia() # Para sabermos se a pilha está vazia ou não

print("Pilha está vazia?") # Está vazia ou não?

if esta_vazia == True: # Aqui espondo essa pergunta em português
    print("Sim")
else:
    print("Não")

print("Tamanho da pilha:", pilha.tamanho()) # Aqui imprimimos a quantidade de elementos que tem na pilha

print('Elemento na posição requerida:', pilha.elemento(4)) # Elemento na posição tal: se inválida, lança uma exceção

print("Elemento que fora encontrado:", pilha.busca(4))

