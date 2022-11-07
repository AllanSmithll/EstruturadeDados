# 07/11/2022
# Função recursiva que retorna soma de n primeiros termos

def primeiros_termos(n) -> int:
    if n == 0:  # Caso base
        # Se n = 0, retorne 0
        return 0
    else:   # Caso não seja igual a 0
        return n + primeiros_termos(n-1) # aqui é retornado o elemento n somado com a chamada recursiva da função.

        '''
        Assim:
            n + (n-1) + (n-2) ... e assim por diante
        '''

# Principal

print(primeiros_termos(1))
print(primeiros_termos(2))
print(primeiros_termos(3))