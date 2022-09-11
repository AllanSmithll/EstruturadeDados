class Teste:
    __Contador = 0
    def _init__(self, var):
        self.__var = var
        Teste.__Contador += 1

obj = Teste(10)
print(obj.__dict__, obj._Teste__Contador) #Não podemos acessar uma variável privada por meio de referencia ao objeto sem os underlines
#Devemos escrever o Objeto._NomedaClasse__variávelprivada (de classe ou instância)
print(obj._Teste__Contador)
