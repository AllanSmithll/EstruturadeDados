class Cachorro:
    raca = 'Pastor'        #As variáveis de classes podem ser acessadas em toda classe, sendo também variáveis globais
    raca2 = 'Poodle'

    def __init__(self, nome=''):
        self.nome = nome

    #def Raca(self):
        #self.__class__.raca --> Para acessar uma variável de classe,  dentro da própria classe, deve-se escrever dessa forma: self.__class__variavelDeClasse ou NomeDaClasse.variavelDeClasse

c1 = Cachorro('Rex')
c2 = Cachorro('Sheila')
print(f'Nome: {c1.nome}, de raça {c1.raca}.')
print(f'Nome: {c2.nome}, de raça {c2.raca2}.')

#Para acessar uma variável de classe fora da classe, deve-se escrever dessa forma: referenciaAoObjeto.variavelDeClasse ou NomeDaClasse.variavelDeClasse
