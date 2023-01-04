def buscaBinaria(array, chave):
    return buscaBinariaRecursiva(array,chave,0,len(array)-1)
    
def buscaBinariaRecursiva(array, chave, inicio,fim):
    if( inicio > fim):
        return -1
    else:
        meio = (inicio + fim)//2
        if ( chave == array[meio] ):
            return meio # elemento foi encontrado! 
        elif ( chave < array[meio] ):
            return buscaBinariaRecursiva(array,chave,inicio,meio-1)
        else:
            return buscaBinariaRecursiva(array,chave,meio+1,fim)
	

    	
print('Pesquisa: Busca Binária Recursiva')
print('*' * 35)
array = [20,5,15,4,2,9,11]
array = sorted(array)
chave = 12
print('Array de busca:',array)
print('Chave:',chave)
index = buscaBinaria(array,chave)
if( index >= 0):
    print('Chave',chave,'encontrada no indice ',index,'do array')
else:
    print('Chave',chave,'NÃO encontrada no array')
