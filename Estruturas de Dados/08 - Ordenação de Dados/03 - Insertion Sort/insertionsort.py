'''
 A lógica consiste em dividir, virtualmente, um
array em dois conjuntos: um ordenado (Aord) e
um desordenado (Ades)
 O Aord reside no início do array, e a cada
iteração dos elementos de Ades, acrescenta-se
em Aord o elemento na sua posição correta

 Compara-se o elemento j=0 de Ades com os
elementos i de Aord, do final para o início. Se
Ades[j] < Aord[i..0], desloca à direita
'''

def insertionSort(array):
    # percorre o array
    # O laço começa do índice 1, pois o índice 0 é o início
    # do subconjunto ordenado
    for i in range(1, len(array)):
        # chave do subarray desordenado        
        key = array[i]
            
        # Move os elementos de array[0.. i-1] que são maiores
        # do que a chave, para uma posicao à frente de sua
        # posição atual

        j = i-1
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key
	
    	

print('Algoritmo de Ordenação - Inserção Direta')
print('*' * 45)
array = [20,5,15,4,2,9,11]
print('Array Original:',array)
insertionSort(array)
print('Array Ordenado:',array)
