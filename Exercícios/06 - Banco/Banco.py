from Conta import Conta
from typing import List

class OperacaoInvalidaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Banco:
    def __init__(self):
        self.__contas = dict()
        self.__saldoTotal = 0
        self.__moedaCorrente = "R$"
    
    @property
    def acessarConta(self, numero):
        try:
            assert numero in self.__contas
            return self.__moedaCorrente + self.__saldoTotal
        except KeyError:
            raise OperacaoInvalidaException('Acesso a uma conta inválida.')
        
    def sacar(self, numero:int, quantia:float):
        try:
            assert quantia > 0
            # obter o objeto correspondente à conta
            conta = self.__contas[numero]
            if conta.saldo - quantia >= 0:
                conta.saldo -= quantia
            else:
                raise OperacaoInvalidaException(f' Conta {numero}: Saldo insuficiente para saque')
        except KeyError:
            raise OperacaoInvalidaException(f'Conta {numero} não está cadastrada.')
        except AssertionError:
            raise OperacaoInvalidaException(f'Saque: quantia para saque tem que ser maior que {self.__moedaCorrente}0,00.')

    def depositar(self, numero:int, quantia:float):
        "Método que estava faltando, e acabei criando a partir do método de saque."
        try:
            assert quantia > 0
            conta = self.__contas[numero]
            if conta.saldo + quantia > 0:
                conta.saldo += quantia
        except KeyError:
            raise OperacaoInvalidaException(f"Conta {numero} não está cadastrada.")
        except AssertionError:
            raise OperacaoInvalidaException(f"Depósito: quantia inválida para depositar. Tem que ser maior que {self.__moedaCorrente}0,00.")

    def addConta(self, numero:int, titular:str):
        if numero not in self.__contas.keys():
            self.__contas[numero] = Conta(numero,titular)
        else:
            raise OperacaoInvalidaException(f'Conta de numero {numero} já está cadastrada')

    
    def __str__(self):
        s = ''
        cont = 1
        for key in self.__contas.keys():
            s+= f'{cont:02}: {key}, titular {self.__contas[key].titular}, saldo =  {self.__contas[key].saldo}\n'
            cont += 1
        return s

