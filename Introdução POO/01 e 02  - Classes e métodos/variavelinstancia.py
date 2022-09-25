#Variável de instância
class Curso:
    def __init__(self, nome="", periodo=""):
        self.nome = nome                 #Onde tem self.{alguma coisa}, chamasse "variável de instância"
        self.periodo = periodo

    #def getNome(self):       #esses termos acabaram sendo inúteis
     #   return self.nome

    def imprime(self):
        print(f'Curso: {self.nome}\nPeríodo: {self.periodo}') #<-- Podem ser declaradas dentro do método. Porém, só passam a existir depois que o método é chamado

cur1 = Curso()
cur2 = Curso()

cur1.nome = 'TSI'
cur2.nome = 'Redes'
cur1.periodo = '2'
cur2.periodo = '2'

cur1.imprime()
cur2.imprime()