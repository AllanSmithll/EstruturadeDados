def busca_linear_ordenada_recursiva(array,chave):
    return busca_recursiva(array,0,chave)

def busca_recursiva(array, index, chave):
    if index >= len(array):
        return -1

    if ( chave == array[index] ):
        return index # elemento foi encontrado
    else:
        return busca_recursiva(array, index+1, chave)
        
    	
print('Pesquisa: Busca Linear Ordenada')
print('*' * 35)
array = [20,5,15,4,2,9,11]
array = sorted(array)
chave = 7
print('Array de busca:',array)
print('Chave:',chave)
index = busca_linear_ordenada_recursiva(array,chave)
if( index >= 0):
    print('Chave',chave,'encontrada no indice',index,'do array')
