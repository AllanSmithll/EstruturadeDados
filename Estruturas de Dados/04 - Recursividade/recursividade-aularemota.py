# Aula remota de sexta feira, dia 07/10/2022, com Alex Sandro

from email.errors import MultipartConversionError
from platform import java_ver

# Aula de potenciação com recursividade. Neste caso abaixo, fazemos uma chamada indireta

def potenciaYago(base, exp) -> int:
    return potenciaAuxiliar(base,1,exp)

def potenciaAuxiliar(base, exp, limite):
    if exp > limite:
        return 1
    else:
        return base * potenciaAuxiliar(base,exp+1,limite)


'''
1. Há uma regra/padrão que seja geral para a maioria da entrada de dados 
   do problema?
   2 ^ 1 = 1
   2 ^ 2 = 2 x 2
   2 ^ 3 = 2 x 2 x 2
   2 ^ 4 = 2 x 2 x 2 x 2 

   base (2) multiplicada n vezes pelo expoente
   se expoente >= 1 
   ...
2. Identificar os casos bases
   2 ^ 0  = 1
   O caso base é quem vai determinar a quebra do ciclo de chamadas recursivas

3. Ao começar a desenvolver a solução recursiva, certifique-se que um
   dos argumentos de controle de recursividade está sendo alterado
   a cada chamada recursiva, até que atinja o caso base
'''
def potenciaRecursiva(base, exp, n) -> int:   # Temos aqui uma base, um expoente e um "n" que servirá para dizer a ordem da chamada
    print(f'Chamada {n + 1}: base {base}, expoente {exp}')
    if exp == 0:
        return 1
    else:
        return base * potenciaRecursiva(base,exp-1,n+1)

def potenciaIterativa(base, exp):
    resultado = 1
    for i in range(exp):
        resultado *= base
    return resultado

def frec(i,j)->int:
    if i == j:
        return 0
    else:
        return i + frec(i+1,j)
print(frec(2,6)) # o que será exibido


def printNumbersDescending(n):
    if n == 0:
        return
    print(n,end=' ')
    printNumbersDescending(n-1)
printNumbersDescending(10)

def printNumbersAscending(n):
    if n == 0:
        return
    printNumbersAscending(n-1)
    print(n,end=' ')
print()
printNumbersAscending(10)

# main
# 2 ^ 4 = 2 x 2 x 2 x 2
print(potenciaIterativa(2,10))
print(potenciaRecursiva(2,3,0))
print(potenciaYago(2,3))
