def bolha(array):
    for i in range(len(array)-1,0,-1):
        for j in range(0,i):
            if (array[j] > array[j+1] ):
                array[j],array[j+1] = array[j+1],array[j] # Efetua a troca
	    	

print('Algoritmo da Bolha')
print('*' * 36)
array = [20,5,15,4,2,9,11]
print('Array Original:',array)
bolha(array)
print('Array Ordenado:',array)
