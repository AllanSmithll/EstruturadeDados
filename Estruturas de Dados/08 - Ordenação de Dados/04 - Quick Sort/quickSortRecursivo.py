# 11/11/2022
# Quick Sort incompleto

def quickSort(array):
    quickSortRun(array,0,len(array)-1)

def quickSortRun(array,low,high):
    if low < high:
        pi = partition(array,low,high)
        quickSortRun(array, low, pi-1)
        quickSortRun(array, pi+1, high)

def partition(array,low,high):
    pivot = array[low] # pivot
    a = low + 1
    b = high
    ...
    return b