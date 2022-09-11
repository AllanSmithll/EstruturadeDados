class Conta:
    def __init__(self, conta):
        self.conta = conta

a = Conta('Corrente')
print(a.conta) #Acesso a propriedade por meio da referencia ao objeto
