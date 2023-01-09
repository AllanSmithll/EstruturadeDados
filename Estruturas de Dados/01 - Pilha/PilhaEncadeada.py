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

    def estaVazia(self)->bool:
        return self.__start == None

    def tamanho(self)->int:
        '''
        # Percorre todos os nós de uma estrutura linear
        cont = 0
        cursor = self.__head
        while(cursor != None):
            cont += 1
            cursor = cursor.prox
        return cont
        '''
        return self.__tamanho

    def __len__(self)->int:
        return self.__tamanho

    def elemento(self, posicao:int)->any:
        '''
        Retorna a carga armazenada no nó indicado por "posicao"
        '''
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento = self.__tamanho - posicao

            cont = 0
            cursor = self.__start
            while( deslocamento > cont):
                cont += 1
                cursor = cursor.prox

            return cursor.carga
        except AssertionError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
    
    def busca(self, conteudo:any)->int:
        cursor = self.__start
        cont = 0
        while(cursor != None):
            if cursor.carga == conteudo:
                return self.__tamanho - cont
            cont += 1
            cursor = cursor.prox
        raise  PilhaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao:int, conteudo: any):
        try:
            self.__dados[posicao-1] = conteudo
        except IndexError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')

    def empilha(self, conteudo:any):
        self.__dados.append(conteudo)

    def desempilha(self)->any:
        if self.estaVazia():
            raise PilhaException(f'Pilha vazia.')
        return self.__dados.pop()

    def __str__(self):
        s = ''
        for e in self.__dados:
            s+=f'{e} '
        return s

    def esvazia(self):
        self.__dados.clear()
