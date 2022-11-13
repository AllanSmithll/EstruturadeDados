# 12/11/2022
# 1- Selecione o primeiro elemento (i=0) do array
# 2- A partir de i+1, faça a varredura do array e identifique o valor que é menor ao que está armazenado no primeiro elemento
# 3- Troque o valor armazenado no índice do primeiro elemento por aquele determinado como o menor valor
# 4- Ao final da varredura, o menor elemento estará posicionado na primeira posição
# 5- Repetir o procedimento para os n-1 elementos restantes (i = 1, 2, 3, ..., n-1)

def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min] # troca

arrays = [20, 10, 3, 4, 6, 30, 40, 50, 35, 5]
selectionSort(arrays)