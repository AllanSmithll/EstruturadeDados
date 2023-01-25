class SequencialException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Sequencial:
    def __init__(self):
        self.__dados = []
    
    def vazio(self) -> bool:
        return len(self.__dados) == 0
    
    def tamanho(self) -> int:
        return len(self.__dados)

    def inicio(self) -> any:
        if self.vazio():
            raise SequencialException("A fila está vazia.")
        return self.__dados[0]

    def inserir(self, dado):
        self.__dados.append(dado)
    
    def remover(self):
        if self.vazio():
            raise SequencialException("A fila está vazia.")
        return self.__dados.pop(0)

    def __str__(self):
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())

f = Sequencial()
for i in range(1, 6):
    f.inserir(i * 10)
print(f)
f.remover()
print(f)