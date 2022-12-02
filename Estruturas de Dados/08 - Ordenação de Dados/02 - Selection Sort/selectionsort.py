'''
 Selecione o primeiro elemento (i=0) do array
 A partir de i+1, faça a varredura do array e
identifique o valor que é menor ao que está
armazenado no primeiro elemento
 Troque o valor armazenado no índice do
primeiro elemento por aquele determinado
como o menor valor
 Ao final da varredura, o menor elemento estará
posicionado na primeira posição
 Repetir o procedimento para os n-1 elementos
restantes (i = 1, 2, 3, ..., n-1)
'''

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
