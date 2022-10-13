# 10/10/2022

def soma(a, b) -> int:
    ''' Somar os números no intervalo fechado de "a" a "b" '''
    if b == a:
        return a
    else:
        return a + soma(a+1, b)


# Programa principal

print("\n", soma(2, 10))