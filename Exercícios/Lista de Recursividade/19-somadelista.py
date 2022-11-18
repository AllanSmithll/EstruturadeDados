# 18/11/2022, visando a prova 2 de ED que vai ter hoje. Infelizmente, tirei 4 pontos na primeira, mas posso descartá-la se tirar mais que isso
# Faça uma função recursiva que retorne a soma de todos os elementos de um list de inteiros passado como argumento. O protótipo da função é definido por: def soma(lista)

def soma(lista) -> int:
    if len(lista) == 1:  # Caso a lista tenha apenas um elemento
        return lista[0]
    else:
        return lista[0] + soma(lista[1:])  # Caso não, acontece o seguinte:
        '''
        retorna o primeiro elemento + soma(lista[1]) + soma(lista[2]) ... E assim por diante, até acabar o array
        '''

lista = [10, 20, 30, 60]
print(soma(lista))