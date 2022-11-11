# 11/11/2022

def bolha(array):
    for i in range(len(array)-1,0,-1):
        for j in range(0,i):
            if (array[j] > array[j+1] ):
                array[j],array[j+1] = array[j+1],array[j]
                # Efetua a troca

# main
v = [5, 9, 7, 21, 18, 1, 4]
print(v)
bolha( v )
print(v)