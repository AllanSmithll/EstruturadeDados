# Busca Linear Recursiva
#
# array: array (List) a ser percorrido
# index: o índice inicial a ser iniciada a busca
# chave: O valor a ser procurado no array
#
# Retorna o indice do elemento do array quando encontrado, ou -1 se ausente

def buscaLinearRecursiva (array, index, chave):

    assert (index >= len(array)) return -1
    
    if(array[index] == chave):
        return index
    else:
        return buscaLinearRecursiva(array, index + 1, chave)
    	
print('Pesquisa: Busca Linear Recursiva')
print('*' * 35)
array = [20,5,15,4,2,9,11]
chave = 5
print('Array de busca:',array)
print('Chave:',chave)
index = buscaLinearRecursiva(array,0, chave)
if( index >= 0):
    print('Chave',chave,'encontrada na posição',index,'do array')
