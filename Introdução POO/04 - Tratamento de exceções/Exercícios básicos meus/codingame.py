try:
    x = int(input("Numerador: "))
    y = int(input("Denominador: "))
    re = x/y
except ZeroDivisionError:
    print("Divisão por zero inválida.")
except ValueError:
    print("Digite um número inteiro válido")
finally:
    print("FIM!!")