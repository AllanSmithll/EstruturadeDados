#Modulo do medicamento
class Medicamento:
    def __init__(self, nome="", principioAtivo=""):
        self.nome = nome
        self.ativo = principioAtivo

med1 = Medicamento("Histamin", "dexclorfeniramina")
print(Medicamento.__module__) #Todos os arquivos acabam tendo um "main", que é o programa principal, para que o processador execute o processo
