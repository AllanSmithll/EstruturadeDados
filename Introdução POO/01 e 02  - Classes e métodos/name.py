#Propriedade __name__
class Medicamento:
    def __init__(self, nome='', principioAtivo=''):
        self.nome = nome
        self.ativo = principioAtivo

med1 = Medicamento("Histamin", "dexclorfeniramina")
print(Medicamento.__name__)
