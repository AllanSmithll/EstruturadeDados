# 05/12/2022
# Acompanhar código recursivo sem uso de ferramentos computacionais
# Apenas mostrar o resultado do print

def iSR(arr, n): # insertionSortRecursive
    if n<=1:
        return
    
    last = arr[n-1]

    j = n-2

    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
    
    arr[j+1] = last
    print('last:', last, 'array:', arr)  # No exemplo: last: 14 array: [12, 11, 13, 5, 6, 8, 14]

array = [12, 11, 13, 5, 6, 8, 14]
size = len(array)
iSR(array, size)

"""
Acertei e vim comprovar por meio do VS Code
"""