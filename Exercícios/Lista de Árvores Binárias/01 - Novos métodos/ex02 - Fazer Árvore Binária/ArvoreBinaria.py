# 07/11/2022

class No:
    def __init__(self,carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.carga)


class ArvoreBinaria:        
    def __init__(self, carga_da_raiz):
        self.__raiz = No(carga_da_raiz) if carga_da_raiz


    def estaVazia(self)->bool:
        pass
        
    def getRaiz(self)->any:
        pass

    def getCursor(self)->any:
        pass

    def preordem(self):
        pass

    def __preordem(self, no):
        pass

    def emordem(self):
        pass

    def __emordem(self, no):
        pass

    def posordem(self):
        pass

    def __posordem(self, no):
        pass

    def descerEsquerda(self):
        pass

    def descerDireita(self):
        pass


    def resetCursor(self):
        pass

    def addFilhoEsquerdo(self, carga)->bool:
        pass
    
    def addFilhoDireito(self, carga)->bool:
        pass

    def __len__(self):
        pass

    def busca(self, chave ):
        pass
    
    def __busca(self, chave, node):
        pass
        
    def go(self, chave:int ):
        pass
    
    def __go(self, chave:int, node:No)-> No:
        pass

if __name__ == '__main__':
    arv = ArvoreBinaria(2)
    