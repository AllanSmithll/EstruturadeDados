from typing import Any


class ListaException(Exception):
    def __init__(self, msg: str, codErro: int = 0):
        # CodErro:
        # 0: posicao invalida
        # 1: chave de busca não encontrada
        # 2: incompatibilidade de tipo de erro
        super().__init__(msg)
        self.__codErro = codErro


class No:
    def __init__(self, carga: Any):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return str(self.carga)


class Lista:
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self) -> bool:
        return self.__head == None

    def tamanho(self) -> int:
        return self.__tamanho

    def elemento(self, posicao: int) -> Any:
        '''
        Retorna a carga armazenada no nó indicado por "posicao"
        '''
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            cont = 1
            cursor = self.__head
            while (cont < posicao):
                cursor = cursor.prox
                cont += 1

            return cursor.carga
        except AssertionError:
            raise ListaException(
                f'Posicao inválida para a fila atual com {self.tamanho()} elementos')

    def busca(self, conteudo: Any) -> int:
        cursor = self.__head
        cont = 1
        while (cursor != None):
            if cursor.carga == conteudo:
                return cont
            cont += 1
            cursor = cursor.prox
        raise ListaException(f'Valor {conteudo} não está na lista', 1)

    def modificar(self, posicao: int, conteudo: Any):
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            cont = 1
            cursor = self.__head
            while (cont < posicao):
                cursor = cursor.prox
                cont += 1

            cursor.carga = conteudo
        except AssertionError:
            raise ListaException(
                f'Posicao inválida para a lista atual com {len(self)} elementos')

    def inserir(self, posicao: int, carga: Any):
        try:
            assert posicao > 0 and posicao <= self.__tamanho + 1

            novo = No(carga)
            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if (posicao == 1):
                novo.prox = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while ((contador < posicao-1) and (cursor is not None)):
                cursor = cursor.prox
                contador += 1

            novo.prox = cursor.prox
            cursor.prox = novo
            self.__tamanho += 1

        except TypeError:
            raise ListaException('A posição deve ser um número inteiro')
        except AssertionError:
            raise ListaException('Posicao inválida.')
        except:
            raise 

    def remover(self, posicao: int) -> Any:
        try:
            assert posicao > 0 and posicao <= self.__tamanho

            if (self.estaVazia()):
                raise ListaException(
                    'Não é possível remover de uma lista vazia')

            cursor = self.__head
            contador = 1

            while (contador <= posicao-1):
                anterior = cursor
                cursor = cursor.prox
                contador += 1

            carga = cursor.carga

            if (posicao == 1):
                self.__head = cursor.prox
            else:
                anterior.prox = cursor.prox

            self.__tamanho -= 1
            return carga

        except TypeError:
            raise ListaException(f'A posição deve ser um número inteiro')
        except AssertionError:
            raise ListaException(
                f'A posicao deve ser um número entre 1 e {self.__tamanho}')
        except:
            raise

    def __str__(self):
        s = '[ '
        cursor = self.__head
        while (cursor != None):
            s += f'{cursor.carga} '
            cursor = cursor.prox
        s += ']'
        return s