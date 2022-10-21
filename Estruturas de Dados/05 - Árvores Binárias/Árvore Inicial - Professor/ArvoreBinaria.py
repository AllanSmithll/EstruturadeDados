from enum import Enum


class No:
    def __init__(self,carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.carga)


class Origem(Enum):
    RAIZ = 1
    CURSOR = 2

class ArvoreBinaria:        
    def __init__(self, carga_da_raiz: any = None):
        self.__raiz = No(carga_da_raiz) if carga_da_raiz != None else carga_da_raiz
        print(self.__raiz)
        self.__cursor = self.__raiz


    def estaVazia(self)->bool:
        return self.__raiz == None
        
    def getRaiz(self)->any:
        if self.__raiz is not None:
            return self.__raiz.carga
        else:
            return None

    def getCursor(self)->any:
        if self.__cursor is not None:
            return self.__cursor.carga
        else:
            return None

    def preordem(self, origem:Origem = Origem.RAIZ):
        if origem == Origem.RAIZ:
            self.__preordem(self.__raiz)
        elif origem == Origem.CURSOR:
            self.__preordem(self.__cursor)
        
    def __preordem(self, no):
        if no is None:
            return
        print(f'{no.carga}', end=' ')
        self.__preordem(no.esq)
        self.__preordem(no.dir)

    def emordem(self):
        self.__emordem(self.__raiz)

    def __emordem(self, no):
        if no is None:
            return
        self.__emordem(no.esq)
        self.__preordem(no.esq)
        self.__preordem(no.dir)


    def posordem(self):
        pass

    def __posordem(self, no):
        if no is None:
            return
        print(f'{no.carga}', end=' ')
        self.__preordem(no.esq)
        self.__preordem(no.dir)


    def descerEsquerda(self):
        if self.__cursor is not None:
            self.__cursor = self.__cursor

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
    
    def __go(self, chave:int, node:No)->No:
        pass

if __name__ == '__main__':
    arv = ArvoreBinaria(2)
    print('Criada a árvore')
    arv.addFilhoEsquerdo(7)
    arv.addFilhoDireito(5)
    print('Raiz: ', arv.getRaiz())
    print('Cursor: ', arv.getCursor())
    print('Tamanho: ', len(arv))
    arv.descerEsquerda()
    arv.addFilhoEsquerdo(9)
    arv.descerEsquerda()
    arv.addFilhoDireito(3)

    print('Raiz: ', arv.getRaiz())
    print('Cursor: ', arv.getCursor())
    print('Tamanho: ', len(arv))

    arv.resetCursor()
    arv.descerDireita()
    arv.addFilhoEsquerdo(10)

    print()
    arv.preordem()

    print('Raiz: ', arv.getRaiz())
    print('Cursor: ', arv.getCursor())
    print('Tamanho: ', len(arv))

    print('Busca:', arv.busca(3))
    no = arv.go(3)
    print('go:', no)