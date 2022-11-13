from typing import List

def mergeSort(array:List[int]):
    print(array)
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Chamada recursiva para cada metade do array
        mergeSort(right)
        mergeSort(left)

        # Aqui é iniciado o processo de merge dos vetores

        # iteradores para percurso das duas metades
        i = 0 # iterador para a metade esquerda
        j = 0 # iterador para a metade direita
        
        # iterador para o array principal
        k = 0
        
        # Comparando os elementos da metade da esquerda e da direita
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # O valor da metade esquerda é ordenado
              array[k] = left[i]
              # Avança o iterador da metade esquerda
              i += 1
            else:
                # o valor da metade direita é ordenado
                array[k] = right[j]
                # Avança o iterador da metade direita
                j += 1
            # Avança para o próximo slot do array principal
            k += 1

        # Os valores remanescentes, da metade esquerda, são copiados
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # Os valores remanescentes, da metade direita, são copiados
        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1

print('Algoritmo de Ordenação - MergeSort')
print('*' * 45)
#array = [20,5,15,4,2,9,11,3,25,17]
array = [25,48,37,12,57,83,33,92]
print('Array Original:',array)
mergeSort(array)
print('Array Ordenado:',array)
 