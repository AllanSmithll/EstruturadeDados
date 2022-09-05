class Carta:
    def __init__(self, valor, naipe, cor):
        # definir as propriedades da classe
        self.__naipe = naipe
        self.__valor = valor
        self.__cor = cor

    #definindo  um método acessor na sintaxe de python
    @property
    def valor(self):
        return self.__valor

    #definindo o método modificador na sintaxe de python
    '''
    @valor.setter
    def valor(self, novoValor):
        self.__valor = novoValor

    '''
    '''
    def getValor(self):
        return self.__valor
'''

    def getNaipe(self):
        return self.__naipe

    def getCor(self):
        return self.__cor

    def __str__(self):
        return f'{self.__valor} de {self.__naipe}'
