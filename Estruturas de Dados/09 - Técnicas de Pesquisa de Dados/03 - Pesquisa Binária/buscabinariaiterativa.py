def buscaBinaria(array, chave):
    # No inicio, utilizaremos todo o array
    inicio = 0
    fim = len(array)-1
    # Enquanto houver distância entre inicio e fim
    while (inicio <= fim ):
        meio = (inicio + fim)//2
        if ( chave < array[meio] ):
            fim = meio - 1 # Ajusta a posicao final 
        elif ( chave > array[meio] ):
            inicio = meio + 1 #  Ajusta a posicao inicial
        else:
            return meio  # elemento foi encontrado! 
	
    # Se finalizar o laço, percorreu todo o array e não encontrou
    return -1

    	
print('Pesquisa: Busca Binária Iterativa')
print('*' * 35)
array = [20,5,15,4,2,9,11]
array = sorted(array)
chave = 9
print('Array de busca:',array)
print('Chave:',chave)
index = buscaBinaria(array,chave)
if( index >= 0):
    print('Chave',chave,'encontrada na posição',index+1,'do array')
