# MULTIPLAS EXCEÇÕES
# E quando tratamos de múltiplas exceções? Como fica?


try:
    num = int(input("Digite um número: "))
    y = 1/num
    print("Valor de y =", y)
except ZeroDivisionError:   # Nome de uma classe except
    print("Divisão por zero inválida.")  # Nomeado ou não, deve-se ter ao menos um except, se houver try
except ValueError:
    print("Digite um inteiro válido.")
except:  #Tratamento genérico
    print("Erro na operação.")
print("Fim do programa")

# Sendo assim, é possível tratar de várias exceções por meio de vários except

# Bloco ELSE opcional

n = 2
try:
    n = 1 / n
    print("Valor de y =", y)
except ZeroDivisionError:
    print("Divisão por zero inválida.") 
    msg = None
else:
    print("Tudo ocorreu bem.")
    msg = n
finally:
    print("Souka souka")
    msg = n
print(msg)
    