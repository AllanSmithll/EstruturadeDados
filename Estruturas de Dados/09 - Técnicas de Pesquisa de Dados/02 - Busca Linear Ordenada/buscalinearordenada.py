def busca_linear_ordenada(array, chave):
    for i in range(len(array)):
        if ( chave == array[i] ):
            return i # elemento foi encontrado
        elif (chave < array[i]):
            return -1 # interrompe a busca
        
    # Se sair do laço é porque percorreu todo o vetor e não encontrou a chave
    return -1

    	
print('Pesquisa: Busca Linear Ordenada')
print('*' * 35)
array = [20,5,15,4,2,9,11]
array = sorted(array)
chave = 2
print('Array de busca:',array)
print('Chave:',chave)
index = busca_linear_ordenada(array,chave)
if( index >= 0):
    print('Chave',chave,'encontrada na posição',index+1,'do array')
