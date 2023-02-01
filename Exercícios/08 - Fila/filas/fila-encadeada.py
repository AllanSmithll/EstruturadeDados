from typing import Any


class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class NoCabeca:
    def __init__(self) -> None:
        self.inicio = None
        self.final = None
        self.tamanho = 0


class No:
    def __init__(self, carga) -> None:
        self.carga = carga
        self.prox = None

    def __str__(self) -> str:
        return f'{self.carga}'


class Fila:
    def __init__(self) -> None:
        self.__head = NoCabeca()

    def estaVazia(self) -> bool:
        return self.__head.tamanho == 0

    def tamanho(self) -> int:
        return self.__head.tamanho

    def __len__(self) -> int:
        return self.__head.tamanho

    def elemento(self, posicao: int) -> Any:
        try:
            assert posicao > 0 and posicao <= self.__head.tamanho

            cursor = self.__head.inicio
            count = 1
            while (count < posicao):
                cursor = cursor.prox
                count += 1
            return cursor.carga
        except AssertionError:
            raise FilaException(
                f'Posicao inválida para a fila atual com {self.__head.tamanho} elementos')

    def enfileira(self, conteudo: Any) -> None:
        """ novo = No(conteudo)
        self.__head.final.prox = novo
        self.__head.final = novo
        self.__head.tamanho += 1 """

        novo = No(conteudo)

        if self.estaVazia():
            self.__head.inicio = novo
            self.__head.final = novo
        else:
            self.__head.final.prox = novo
            self.__head.final = novo
        self.__head.tamanho += 1

    def busca(self, chave: Any) -> int:  # retornar a posicao de "chave" na fila
        cursor = self.__head.inicio

        count = 0
        while (cursor is not None):
            count += 1
            if cursor.carga == chave:
                return count
            cursor = cursor.prox

        raise FilaException(f'A chave {chave} não está na Fila.')

    def desenfileira(self) -> Any:
        if self.estaVazia():
            raise FilaException(f'Fila vazia. Não é possivel a remocao')

        carga = self.__head.inicio.carga
        self.__head.inicio = self.__head.inicio.prox
        self.__head.tamanho -= 1
        return carga

    def __str__(self) -> str:
        s = '[ '
        cursor = self.__head.inicio

        while (cursor is not None):
            s += f'{cursor.carga} '
            cursor = cursor.prox

        s += ']'

        return s

    def esvazia(self) -> None:
        """ self.__ocupados = 0
        self.__frente = 0
        self.__final = -1 """

        """ self.__head.inicio = None
        self.__head.final = None
        self.__head.tamanho = 0 """

        while (not self.estaVazia()):
            self.desenfileira()

    def combina(cls, fres, f1, f2):
        