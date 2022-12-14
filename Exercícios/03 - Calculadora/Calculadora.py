import sys


class Calculadora:
    #Construtor
    def __init__(self, registrador: float = None):
        if registrador is None:
            self.__registrador = 0.0
        else:
            self.__registrador = registrador
        self.historico = self.__registrador

    #deletor
    def __del__(self):
        print(f'Objeto com endereço de memória {hex(id(self))} deletado.', 
            file = sys.stderr)
    
    #getter
    @property
    def registrador(self):
        return self.__registrador
    
    #Magic Methods
    def __str__(self):
        return f'Total: {self.__registrador}'
    
    #Funções da calculadora
    def adicionar(self, valor=float):
        self.__definir_historico()
        self.__registrador += valor
    def subtrair(self, valor:float):
        self.__definir_historico()
        self.__registrador -= valor
    def dividir(self, valor:float):
        self.__definir_historico()
        try:
            self.__registrador /= valor
        except ZeroDivisionError:
            self.__registrador = 0.0
    def multiplicar(self, valor:float):
        self.__definir_historico()
        self.__registrador *= valor
    def exibir(self):
        print(self.__registrador)
    def resetar(self):
        self.__definir_historico()
        self.__registrador = 0.0
    def desfazer(self):
        self.__registrador, self.__historico = self.__historico, self.__registrador
    
    #Métodos auxiliares
    def __definir_historico(self):
        self.__historico = self.__registrador
