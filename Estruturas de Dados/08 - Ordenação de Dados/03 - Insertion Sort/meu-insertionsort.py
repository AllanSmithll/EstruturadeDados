# 30/07/2023 - FRACASSO

def insertion(array):
    array_auxiliar = []
    if len(array) <= 1:
        return array
    else:
        array_auxiliar.append(array[0])
        for i in range(1,len(array)): # desordenado
            for j in range(len(array_auxiliar)): # ordenado
                if array[i] >= array_auxiliar[j]:
                    array_auxiliar.append(array[i])
                else:
                    array_auxiliar.insert(j,array[i])
    return array_auxiliar

array_teste = [10,5,6,7,3,4,11,2,1,9,8]
insertion(array_teste)