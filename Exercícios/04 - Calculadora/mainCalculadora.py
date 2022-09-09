from fcntl import I_CANPUT
from Calculadora import Calculadora

calculadora = Calculadora()
operacao = None
while True:
    print("+---------------+",
            f"| {calculadora.registrador: >13} |",
            "+---------------+",
            "(+) somar",
            "(-) subtrair",
            "(/) dividir",
            "(*) multiplicar",
            "(r) resetar",
            "(d) desfazer",
            "(exit) sair",
            "---------------",
            sep="\n")
    operacao = input("Operação: ")

    try:
        if operacao == '+':
            valor = float(input("Valor"))
            calculadora.adicionar(valor)
            continue
        elif     