# 10/10/2022

def maior(array) -> float:
    ''' Qual o maior valor do array '''
    if len(array) == 0:
        raise Exception("Array vazio. Não pode.")
    if len(array) == 1:
        return array[0]
    retorno = maior(array[1:])
    if array[0] > retorno:
        return array[0]
    else:
        return retorno

# Principal
rating = [2.5, 6.0, 4.3, 2.8, 10.5, 3.5, 5.3]
print(maior(rating))