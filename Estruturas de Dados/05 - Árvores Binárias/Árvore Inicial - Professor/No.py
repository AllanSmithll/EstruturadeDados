# Classe que serve como criador do nó, ou carga
class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return f'{self.carga}'