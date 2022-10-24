# 23/10/2022
'''
Regra:

No mínimo h + 1, e no máximo 2h + 1 - 1, utilizando uma árvore binária

'''

class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self) -> str:
        return f"{self.carga}"
No(20)