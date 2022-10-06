class Conta:
    # construtor parametrizado da classe
    def __init__(self, agencia, conta):
        self.agencia = agencia
        self.conta = conta
        self.digito = self.__geraDigito(conta)
        self.__saldo = 1000
    
    # método de instância público
    def sacar(self, valor):
        assert self.__saldo - valor >= 0
        self.__saldo -= valor

    # método de instância privado
    def __geraDigito(self, conta):
        soma = 0
        for d in conta:
            soma += int(d)
        return soma % 11

    
    def __str__(self):
        return f'Conta {self.conta}-{self.digito}, Agencia: {self.agencia}, Saldo: {self.__saldo}'

if __name__ == '__main__':
    c1 = Conta('1010','4561')
    print(c1)
    c1.sacar(200 )
