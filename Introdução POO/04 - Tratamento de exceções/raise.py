# raise *nomeDaExceçãoVálida* ou
# raise

def fproblema(var):
    raise ZeroDivisionError   # Exceção sendo lançada
try:
    fproblema()
except ArithmeticError:     # Capturada por ArithmeticError
    print("Erro de divisão.")


def fproblema(var):
    try:
        return 1/var
    except ZeroDivisionError:
        print("Erro de divisão.")
        raise    # probagando a mesma exceção
try:
    fproblema(0)
except ZeroDivisionError:       # tratando em outra parte do código
    print("Erro de divisão.")

print("Fim")