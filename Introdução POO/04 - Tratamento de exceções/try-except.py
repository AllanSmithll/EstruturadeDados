# 01/10/2022
# Estrutura básica do try-except
'''
try:
    instrução1
    instrução2
    instrução3
    ...
    instrução(n)
except:
    instrução x
    ...
    instrução z
Instrução após o try-except (segue o fluxo)
'''

# Vamos ver como seria o erro da divisão por zero em programação estruturada
# Usaremos o exemplo da divisão por zero. Queremos que quando isso aconteça, mostre a mensagem "DIVISÃO POR ZERO NÃO PERMITIDA"

a = int(input())
b = int(input())
if (b != 0 ):
    print( a / b )
else:
    print('Divisão por zero não permitida')
print('Programa finalizado com sucesso! ') 

# O ruim dessa forma de programar é que, mesmo que o erro já aconteça na estrutura de decisão, o programa ainda assim é executado como se nada de ruim estivesse acontecendo.
# Como assim? Vamos ver outra forma de resolver essa questão da DIVISÃO POR ZERO com POO

a = int(input("a: "))
b = int(input("b: "))
try:
    print( a / b )
    print("Operação realizada com sucesso!") # Veja que tiramos os if e else
except:
    print('Divisão por zero não permitida')

# Quando damos run usando try-except, e então fazemos uma divisão por 0, o print da linha 35 de try acaba sendo ignorado, e lança a frase: "DIVISÃO POR ZERO NÃO PERMITIDA", do except