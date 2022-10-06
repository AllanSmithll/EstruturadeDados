class ContaBloqueadaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Conta:
    # construtor parametrizado da classe
    def __init__(self, agencia, conta):
        self.agencia = agencia
        self.conta = conta
        self.digito = self.__geraDigito(conta)
        self.saldo = 0
        self.bloqueado = False
    
    # método de instância público
    def sacar(self, valor):
        if self.bloqueado == True:
            raise ContaBloqueadaException('Não é possível sacar pois a conta do cliente está bloqueada')

        assert self.saldo - valor >= 0, 'Saldo insuficiente para saque'
        self.saldo -= valor

    # método de instância privado
    def __geraDigito(self, conta):
        soma = 0
        for d in conta:
            soma += int(d)
        return soma % 11

    
    def __str__(self):
        return f'Conta {self.conta}-{self.digito}, Agencia: {self.agencia}, Saldo: {self.saldo}'

if __name__ == '__main__':
    c1 = Conta('1010','4561')
    print(c1)
    try:
        c1.saldo = 500
        c1.bloqueado = True
        c1.sacar(100)
        print(c1)
    except AssertionError as ae:
        print(ae)
    except ContaBloqueadaException as cbe:
        print(cbe)