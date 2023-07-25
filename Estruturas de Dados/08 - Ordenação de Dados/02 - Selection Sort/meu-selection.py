# 25/07/2023

def selection(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min]

array_teste = [10,5,6,7,3,4,2,1,9,8]
selection(array_teste)
print(array_teste)