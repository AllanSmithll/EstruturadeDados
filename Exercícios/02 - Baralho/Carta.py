class Carta:
    def __init__(self, naipe, cor, valor):
        self.__naipe = naipe
        self.__cor =  cor
        self.__valor = valor
    
    #definindo um método acessor (get) na sintaxe de Python *Lembrando: get() recupera o valor de uma propriedade privada
    @property
    def valor(self):
        return self.__valor

    #Definindo o método modificador na sintaxe de Python *Lembrando: set() modifica o valor de uma probriedade privada
    '''
    @valor.setter
    def valor(self, novoValor):
        self.__valor = novoValor
    '''
    '''
    def getValor(self):   #Faz exatamente a mesma coisa da linha 8 em diante
        return self.__valor
    '''
    def getNaipe(self):
        return self.__naipe

    def getCor(self):
        return self.__cor

    def __str__(self):
        return f'{self.__valor} de {self.__naipe}'