from No import No


class ArvoreBinaria:
    def __init__(self, carga_raiz:any = None):
        self.__raiz = No(carga_raiz) if carga_raiz != None else carga_raiz
        print(self.__raiz)
        self.__cursor = self.__raiz

    def criarRaiz(self, carga_raiz:any):
        pass