'''
#MÉTODOS GET() E SET()

get() -> recupera o valor de uma propriedade privada

def get<nome_atributo_privado>(self):
    return self.__<nome_atributo_privado>

Exemplo:
'''

def getNome(self):
    return self.__nome

print(getNome())

"""
set() modifica o valor de uma propriedade privada

def set<att_privada>(self, novoValor): 
    self.__<att_privado> = novoValor

Exemplo:
"""

def setNome(self, novoValor):
    self.__nome = novoValor

