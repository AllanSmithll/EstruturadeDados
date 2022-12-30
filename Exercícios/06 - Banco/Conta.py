class Conta:
    def __init__(self, numero:int, titular:str):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 100.00

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @numero.setter
    def numero(self, novoNumero):
        self.__numero = novoNumero

    @titular.setter
    def titular(self, novoTitular):
        self.__titular = novoTitular

    @saldo.setter
    def saldo(self, novoSaldo):
        assert novoSaldo >= 0, 'Saldo não pode ser um valor negativo'
        self.__saldo = novoSaldo

    def __str__(self):
        return f'conta {self.__numero}, titular: {self.__titular}, saldo = {self.__saldo:5.2f}'


