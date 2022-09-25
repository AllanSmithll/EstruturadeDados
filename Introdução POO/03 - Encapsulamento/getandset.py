'''
#MÉTODOS GET() E SET()

get() -> recupera o valor de uma propriedade privada

def get<nome_atributo_privado>(self):
    return self.__<nome_atributo_privado>

Exemplo:
'''

"""def getNome(self, nome=""):
    return self.__nome

print(getNome("Allan"))


set() modifica o valor de uma propriedade privada

def set<att_privada>(self, novoValor): 
    self.__<att_privado> = novoValor

Exemplo:
"""

def setNome(self, novoValor):
    self.__nome = novoValor

'''@property  para getters
def <atributoPrivado>(self):
    return self.__<att_privado'''

print("\nFORMA PARTICULAR DE PYTHON PARA GET/SET\n")

class Disciplina:
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome #Acessa o valor da variável para retorná-la

    @nome.setter
    def nome(self, n):
        self.__nome = n  #Modifica o valor da variável

d = Disciplina('POO')
d.nome = "Estrutura de Dados" #set implícito
print(d.nome) #get implícito


