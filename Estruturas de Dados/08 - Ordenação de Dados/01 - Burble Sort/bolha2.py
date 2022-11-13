def bolha(array):
    for i in range(len(array)-1,0,-1):
        troca = False
        for j in range(0,i):
            if (array[j] > array[j+1] ):
                array[j],array[j+1] = array[j+1],array[j] # Efetua a troca
                troca = True
        if( not troca ): # não houve troca
            return
	    	

print('Algoritmo da Bolha com flag de Troca')
print('*' * 36)
array = [20,5,15,4,2,9,11]
print('Array Original:',array)
bolha(array)
print('Array Ordenado:',array)
