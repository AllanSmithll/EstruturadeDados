# 15/10/2022
# INVERTER A STRING DO PROGRAMA PRINCIPAL

def printInverse(str) -> str:
    if (str == ''): 
    # Caso base de parada: retorne quando a string estiver vazia
        return
    printInverse(str[1:])  
    ''' Faz a chamada do método, pegando cada um dos elementos da string,
     até chegar na condição base. Quando não tiver mais elementos para analisar,
      chegar ao caso base, retorne '''
    print(str[0], end='')
    ''' Depois de ter retornado todos os outros elementos da pilha de chamadas,
    retorne também o elemento do primeiro índice '''

string = "João"
printInverse(string)