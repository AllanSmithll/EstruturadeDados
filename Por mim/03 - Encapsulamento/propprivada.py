class Teste:
    __Contador = 0
    def _init__(self, var):
        self.__var = var
        Teste.__Contador += 1

obj = Teste(10)
print(obj.__dict__, obj._Teste__Contador)
# quebrando o encapsulamento de uma variável
# privada
print(obj._Teste__Contador)
