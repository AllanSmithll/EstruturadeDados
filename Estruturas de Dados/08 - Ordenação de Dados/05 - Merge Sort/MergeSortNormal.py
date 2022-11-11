# 11/11/2022
# Merge Sort Incompleto

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        # chamada recursiva para a divisão
        mergeSortList(right)
        mergeSortList(left)
        # merge...
        # Examine o código
        ...