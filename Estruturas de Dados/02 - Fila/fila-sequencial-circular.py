"""class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class FilaCircular:
    def __init__(self, tamanho: int = 10):
        self.__frente = 0
        self.__final = -1
        self.__tamanho = tamanho
        self.__ocupados = 0
        self.__dados = [None for i in range(tamanho)]

    def vazia(self) -> bool:
        return self.__ocupados == 0

    def cheia(self):
        return self.__ocupados == self.__tamanho
    
    def tamanhoAtual(self) -> int:
        return self.__ocupados
    
    def __len__(self) -> int:
        return self.__ocupados

    def elemento(self, posicao: int) -> any:
        try:
            assert posicao > 0 and posicao <= self.__ocupados
            inicio = self.__frente
            for i in range(posicao - 1):
                inicio = (inicio + 1) % self.__"""