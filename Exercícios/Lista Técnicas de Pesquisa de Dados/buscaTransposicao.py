# 13/12/2022
# Criar um método de busca para implementação, com uma modificação para o caso de não encontrar a chave: "chave não encontrada" ao invés de KeyError

class ChaveInvalidaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def buscaTransposicao(chave:int, array:list[int]) -> int:
    '''Método #1 que tem o objetivo de deslocar os elementos mais acessados para o início do array. Quando acessado por último, o valor do array ficará na primeira posição.'''

    inicio=0
    fim=len(array)-1

    while inicio <= fim:
        meio = (inicio+fim)//2
        
        if chave > array[meio]:
            inicio = meio + 1
        elif chave < array[meio]:
            fim = meio - 1
        else:
            return meio

    return ChaveInvalidaException("chave não encontrada.")

#=================== #
# PROGRAMA PRINCIPAL #
#=================== #

print('\nBusca Por Transposição')
print('*' * 35)
array = [2, 3, 23, 10, 40, 27, 49, 38, 20]
array = sorted(array)
print("Array:", array)
chave = int(input("Chave a ser encontrada: "))
index = buscaTransposicao(chave, array)

print("\nChave", chave,"no índice", index, "do array.")
