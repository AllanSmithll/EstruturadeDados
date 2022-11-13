from typing import List

def insertionSort(array):
    insertionSortRecursivo(array, len(array))

def insertionSortRecursivo(array:List[int], n:int):
    # caso base
    if n <= 1:
        return
     
    # Ordena os primeiros n-1 elementos
    insertionSortRecursivo(array,n-1)

    '''Insere o último elemento na sua posição correta no
       array ordenado.'''
    ultimo = array[n-1]
    j = n-2
     
    # Move os elementos de array[0..i-1], que são maiores
    # do que a chave, para a posição subsequente de sua
    # posição atual
    while (j>=0 and array[j]>ultimo):
        array[j+1] = array[j]
        j = j-1
 
    array[j+1]=ultimo


    	

print('Algoritmo de Ordenação - Inserção Direta')
print('*' * 45)
array = [20,5,15,4,2,9,11]
print('Array Original:',array)
insertionSort(array)
print('Array Ordenado:',array)
