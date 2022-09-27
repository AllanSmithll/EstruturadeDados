def a():
    print('1')
    b()

def b():
    print("2")
    c()

def c():
    print("3")
    d()

def d():
    print("4 ")


print("Início")
a()
b()
print("Fim")