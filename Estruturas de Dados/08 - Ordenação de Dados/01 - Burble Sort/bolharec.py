
def bolhaRecursiva(array):
    executaBolha(array,len(array))

def executaBolha(array,size):
    troca = False
    for j in range(size-1):
        if (array[j] > array[j+1] ):
            temp = array[j]
            array[j] = array[j+1] # Efetua a troca
            array[j+1] = temp
            troca = True
    if (troca):      # Houve troca 
        executaBolha(array,size-1)

	    	
print('Algoritmo da Bolha Recursivo')
print('*' * 36)
array = [20,5,15,4,2,9,11]
print('Array Original:',array)
bolhaRecursiva(array)
print('Array Ordenado:',array)
