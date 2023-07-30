# 25/07/2023

def selection(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min]

array_teste = [10,5,6,7,3,4,2,1,9,8]
selection(array_teste)
print(array_teste)

def letraMaisFrequente(p_string:str) -> str:
    '''
    \rletraMaisFrequente(p_string) \n
    \rp_string: string que será analisada pela função \n
    Função que retorna o caracter que mais aparece na string, exceto os espaços'''
    caracteres = {}
    for carac in p_string.strip():
        if (carac in caracteres and carac != '  '):
            caracteres[carac] += 1
        if (carac not in caracteres and carac != ' '):
            caracteres[carac] = 1
        else:
            continue
    letra_mais_frequente = max(caracteres, key=caracteres.get)
    return letra_mais_frequente

str = 'This is Elon Musk'
print(letraMaisFrequente(str))
