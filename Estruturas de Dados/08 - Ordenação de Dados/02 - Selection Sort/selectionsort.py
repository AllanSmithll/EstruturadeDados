def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):          
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min] # troca
	
    	

print('Algoritmo de Ordenação - Seleção Direta')
print('*' * 45)
array = [20,5,15,4,2,9,11]
print('Array Original:',array)
selectionSort(array)
print('Array Ordenado:',array)
