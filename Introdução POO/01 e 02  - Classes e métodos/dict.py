class Medicamento:
    preço = 0.00
    def __init__(self, nome='', PrincipioAtivo=''):
        self.nome = nome
        self.ativo = PrincipioAtivo

med1 = Medicamento('Xarope', 'Histamine')
print(med1.__dict__) #--> Dicionário mostra os nomes e valores de todas as propriedades de med1, o objeto
print(Medicamento.__dict__) #--> Aqui, o dicionário o observa as variáveis de classe (e definições de métodos)
