class Dog:
    raca = 'Pastor Alemão'  #Essa linha representa a variável da classe inteira
    raca2 = 'Poodle'

    def __init__(self, nome): #Se for acessar dentro da classe, escreve-se: NomeDaClasse.variavelDeClasse ou self.__class__.variavelDeClasse
        self.nome = nome

c1 = Dog('Rex')
c2 = Dog('Sheila')
print(f'Nome: {c1.nome}, de raça {c1.raca}.')
print(f'Nome: {c2.nome}, de raça {c2.raca2}.') #Para acessar uma variável de classe fora da classe, é necessário escrever algo como: refêrenciaAoObjeto.variavelDeClasse ou NomeDaClasse.variavelDeClasse
