# 05/11/2022
# 1- Selecione o primeiro elemento (i=0) do array
# 2- A partir de i+1, faça a varredura do array e identifique o valor que é menor ao que está armazenado no primeiro elemento
# 3- Troque o valor armazenado no índice do primeiro elemento por aquele determinado como o menor valor
# 4- Ao final da varredura, o menor elemento estará posicionado na primeira posição
# 5- Repetir o procedimento para os n-1 elementos restantes (i = 1, 2, 3, ..., n-1)

def selectionSortRec(array):
    __executaSelectionSort(array, len(array))

def __executaSelectionSort(array, size):
    troca = False
    for i in range(len(array)-1): # Vamos fazer iterações regressivas
        if array[i] > array[i+1]: # Se o elemento referenciado for maior que o elemento que está ao seu lado
            temp = array[i] # Crio a variável temp e atribuo o valor array[i]
            array[i] = array[i+1] #\ Array na posição i recebe o elemento ao seu lado
            array[i+1] = temp # O elemento ao seu lado recebe o elemento temp (array[i])
            troca = True # Houve troca de posição
        if (troca): # Se troca = True
            __executaSelectionSort(array, size-1) # Chame de novo a função

arrays = [20, 10, 5, 30, 5, 6]
print("Array original:", arrays)
selectionSortRec(arrays)
print("Array após o Selection Sort:", arrays)

'''
Questão 01 da lista concluída com sucesso
'''