# Feito por mim em 25/11/2022
'''
 Quando dois elementos estão fora de ordem, é
feita a inversão e estes são trocados de posição
 Primeiro elemento é comparado com o segundo,
o segundo com o terceiro, o terceiro com o
quarto, ...
    -> Inversões são executadas quando necessárias
 Fim da comparação: quando o penúltimo é
comparado com o último
    -> Ao final da varredura, o maior elemento ficará
posicionado na última posição
 O processo continua até n-i, até que todo o
vetor esteja ordenado (i = 1, 2, 3, ...)'''

def bolha(array): # Funão bolha
    for i in range(len(array)-1, 0, -1):
        for j in range(0, i):
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j] # E assim é feita a troca


lista = list()
lista = [1, 20, 34, 4, 9, 8, 45, 2, 69]
print("Array inicial:", lista)
bolha(lista)
print("Array ordenado:", lista)