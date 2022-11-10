class No:
    def __init__(self, carga):
        self.carga = carga
        self.esquerda = None
        self.direita = None
    def __str__(self) -> str:
        return f'{self.carga}'
        

class ArvoreBinaria:
    def __init__(self, carga_da_raiz:any = None):
        self.__raiz = No(carga_da_raiz) if carga_da_raiz != None else carga_da_raiz
        print(self.__raiz)
        self.__cursor = self.__raiz