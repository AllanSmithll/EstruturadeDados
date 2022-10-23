# 22/10/2022

'''
Por mais incrível que pareça, ainda vou codar sobre "Recursividade", mas abaixo já é possível um exemplo deste recurso, até porque há um "chamamento entre os métodos
'''

def a(): # Definimos o método a, que imprimirá o número 1, depois chamar b()
    print('1')
    b() 

def b(): # Chama o método b, que imprimirá 2, depois chamar c()
    print("2")
    c()

def c():   # Chama o método c, que imprimirá 3, depois que chama d()
    print("3")
    d()

def d():   # Por fim, o método d, que entregará o "print('4\n')" a quem o chamou
    print("4\n")


print("Início")
a()
b()
c()
d()
print("Fim")