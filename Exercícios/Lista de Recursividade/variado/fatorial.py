# 09/11/2022
# Minha solução fatorial para estudar pra prova

def fatorial(n) -> int:
    if n == 0:   # Caso base em que fatorial de 0 sempre é 1
        return 1
    else:
        return (n * fatorial(n-1))     # Se não for zero, faço uma multiplicação de n (por exemplo, 5) pela chamada fatorial (no caso, seria fatorial de n - 1, 4).
        # Porém, não será feita apenas uma chamada. Depois que chama a função pela primeira vez, será novamente testado nas condições. Se n = 0, retorno 1. Se não, entro de novo na estrutura ELSE.

if __name__ == '__main__':
    numero = int(input("Fatorial de: "))
    print(fatorial(numero))
