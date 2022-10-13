# 09/10/2022
# Cálculo do fatorial a partir do uso da recursividade


# Solução iterativa (a mais comum, sem recursividade)

def fatorial( n ):
    if ( n == 0 ):  # "Se n for igual a 0, retorne 1" é o caso base, ou exceção da fórmula
        return 1
    fat = 1
    for i in range(n, 0,-1):
        fat *= i
    return fat

# Solução recursiva

def fatorial(n):
    if (n == 0):
        return 1
    x = n - 1     # Aqui eu faço o uso da fórmula geral, onde o próximo elemento da multiplicão fatorial é igual a n - 1
    y = fatorial(x)   # Então eu chamo o método fatorial para que y receba o resultado da fatorial de x, em que x é igual a n - 1
    return (n * y)    # n! = n * (n - 1)!


print(fatorial(4))
