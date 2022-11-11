# 11/11/2022

def insertionSort(array):
    for i in range(1,len(array)):
        chave = array[i]
        j = i-1
        while j>=0 and chave < array[i]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = chave

# main
v = [5, 9, 7, 21, 18, 1, 4]
print(v)
insertionSort( v )
print(v)