# 25/07/2023 - estudos de ED depois do segundo período

def bolha(array):
    for i in range(len(array)-1,0,-1):
        for j in range(0,i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j +1], array[j]
                
array_teste = [10,5,6,7,3,4,2,1,9,8]
bolha(array_teste)
print(array_teste)