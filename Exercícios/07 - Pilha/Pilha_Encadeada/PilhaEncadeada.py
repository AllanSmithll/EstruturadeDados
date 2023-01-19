class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class No:
    def __init__(self, carga: any):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return str(self.carga)


class Pilha:
    def __init__(self):
        self.__start = None
        self.__tamanho = 0

    def estaVazia(self) -> bool:
        return self.__start is None

    def tamanho(self) -> int:
        '''
        # Percorre todos os nós de uma estrutura linear
        cont = 0
        cursor = self.__head
        while(cursor != None):
            cont += 1
            cursor = cursor.prox
        return cont
        '''
        cont = 0
        cursor = self.__start
        while (cursor is not None):
            cont += 1
            cursor = cursor.prox
        self.__tamanho = cont
        return self.__tamanho

    def __len__(self) -> int:  # len(Pilha()) -> self.__tamanho
        return self.__tamanho

    def elemento(self, posicao: int) -> any:
        '''
        Retorna a carga armazenada no nó indicado por "posicao"
        '''
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento = self.__tamanho - posicao

            cont = 0
            cursor = self.__start
            while(deslocamento > cont):
                cont += 1
                cursor = cursor.prox

            return cursor.carga
        except AssertionError:
            raise PilhaException(
                f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')

    def busca(self, conteudo: any) -> int:
        '''
        Retorna a posição do nó cuja carga é igual a "conteudo"
        '''
        cursor = self.__start
        cont = 0
        while(cursor is not None):
            if cursor.carga == conteudo:
                return self.__tamanho - cont  # retorne a posição de "conteudo"
            cont += 1
            cursor = cursor.prox
        raise PilhaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao: int, conteudo: any):  # modificar o conteúdo de uma posição
        """
        try:
            self.__dados[posicao-1] = conteudo
        except IndexError:
            raise PilhaException(
                f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
        """
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento = self.__tamanho - posicao

            cont = 0
            cursor = self.__start
            while (deslocamento > cont):
                cont += 1
                cursor = cursor.prox

            cursor.carga = conteudo
        except AssertionError:
            raise PilhaException(
                f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')

    def empilha(self, conteudo: any):
        novo = No(conteudo)
        novo.prox = self.__start
        self.__start = novo
        self.__tamanho += 1

    def desempilha(self) -> any:
        if self.estaVazia():
            raise PilhaException('Pilha vazia')
        carga = self.__start.carga
        self.__start = self.__start.prox
        self.__tamanho -= 1
        return carga
        """
        if self.estaVazia():
            raise PilhaException(f'Pilha vazia.')
        return self.__dados.pop()
        """

    def __str__(self) -> str:
        s = ''
        # o start não pode mudar de lugar. Portanto precisamos utilizar "cursor"
        cursor = self.__start
        while (cursor is not None):
            s += f'{cursor.carga} '
            cursor = cursor.prox
        return s

    def esvazia(self):
        # self.__start = None # -> só em python

        while (not self.estaVazia()):
            self.desempilha()

        """
        try:
            while (self.desempilha()):
                pass
        except:
            pass
        """

    def __getStart(self) -> No:
        return self.__start

    def inverte(self) -> bool:
        if self.__tamanho <= 1:
            return False

        pilhaInvertida = Pilha()
        cursor = self.__start
        carga = None
        while (cursor is not None):
            carga = self.desempilha()
            pilhaInvertida.empilha(carga)
            cursor = cursor.prox
        self.__start = pilhaInvertida.__getStart()

        return True

    def subTopo(self) -> any:
        subTopo = self.__start.prox
        if subTopo is None:
            raise PilhaException('A pilha não possui sub-topo.')
        return subTopo.carga

    def topo(self) -> any:
        if self.estaVazia():
            raise PilhaException(f'Uma pilha vazia não possui topo.')
        return self.__start.carga

    def desempilha_n(self, n: int) -> bool:
        if n > self.__tamanho:
            return False
            """
            raise PilhaException(
                f'Não é possível desempilhar {n} elementos de uma pilha com {self.__tamanho} elementos') 
            """

        for i in range(n):
            self.desempilha()
        return True

    def obtemBase(self) -> int:
        if self.estaVazia():
            raise PilhaException('Esta pilha não possui base (vazia)')
        cursor = self.__start

        while (cursor.prox is not None):
            cursor = cursor.prox

        return cursor

    def concatena(self, outraPilha: 'Pilha') -> None:
        pilhaAux = Pilha()
        # Inverter a pilha "outraPilha"
        while (not outraPilha.estaVazia()):
            pilhaAux.empilha(outraPilha.desempilha())
        # descarregando paux na pilha que recebeu a chamada
        while (not pilhaAux.estaVazia()):
            self.empilha(pilhaAux.desempilha())

        """ 
        # utilizando o método inverte
        outraPilha.inverte()
        while (not outraPilha.estaVazia()):
            self.empilha(outraPilha.desempilha())
        """