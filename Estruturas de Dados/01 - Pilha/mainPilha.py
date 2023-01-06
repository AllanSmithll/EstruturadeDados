# Análise finalizada em 06/01/2023

from PilhaSequencial import *

numeros = [4,5,6,90,56,31,42,57] # Lista a ser empilhada

pilha = Pilha() # Crio um objeto pilha para usar
for n in numeros:
    pilha.empilha(n) # Empilho cada elemento da lista "numeros"

print('Array: ',numeros)  # Imprimo o array inicial
print('A pilha ficou assim: ', pilha) # A pilha depois que utilizei do método "empilha()"

esta_vazia = pilha.estaVazia() # Para sabermos se a pilha está vazia ou não

print("Pilha está vazia?") # Está vazia ou não?

if esta_vazia == True: # Aqui respondo essa pergunta em português
    print("Sim")
else:
    print("Não")

print("Tamanho da pilha:", pilha.tamanho()) # Aqui imprimimos a quantidade de elementos que tem na pilha

print('Elemento na posição requerida:', pilha.elemento(4)) # Elemento que está na posição tal: se inválida, lança uma exceção

print("Elemento que fora encontrado:", pilha.busca(4)) # O índice que foi encontrado o elemento posto no argumento da busca(). Se Não existe na pilha, chama a exceção

pilha.modificar(5, 60) # Modifiquei o elemento na posição 5 e coloquei 60 no lugar

print(f"Pilha modificada na posição 5. Ficou assim: {pilha}")

pilha.desempilha() # Agora irei desempilhar um elemento de "pilha"

print(pilha)

pilha.esvazia() # Agora terminarei as práticas de código com o método "esvazia" para esvaziar toda pilha

if pilha.estaVazia():
    print("\nA pilha analisada está vazia. Fim dos testes.")

