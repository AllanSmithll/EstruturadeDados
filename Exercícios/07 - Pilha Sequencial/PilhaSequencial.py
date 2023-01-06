class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Pilha:
    def __init__(self):
        self.__dados = list()  # A Pilha é uma lista de dados que a adição e a remoção se dão em uma das extremidades

    def estaVazia(self)-> bool:
        '''Método para dizer se a pilha está vazia ou não'''
        return len(self.__dados) == 0  # Está vazia 

    def tamanho(self)->int:
        '''Método para sabermos quantos elementos tem na pilha'''
        return len(self.__dados)

    def __len__(self)->int:
        '''Método para sabermos o tamanho da pilha'''
        return len(self.__dados)

    def elemento(self, posicao:int)->any:
        '''Método que devolve um elemento em determinada posição

        Argumentos:

        posicao: posição em que é solicitado um elemento.
        '''
        try:
            return self.__dados[posicao-1]
        except IndexError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
    
    def busca(self, conteudo:any)->int:
        '''Método que busca o índice de determinado elemento

        Argumentos:

        conteudo: o elemento que é buscado pelo usuário
        '''
        for i in range(len(self.__dados)):
            if self.__dados[i] == conteudo:
                return i+1
        raise  PilhaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao:int, conteudo: any):
        '''
        Modifica o elemento de tal posição visual na pilha
        
        Argumentos:
        
        posicao: posição em que foi solicitada a modificação
        conteudo: o elemento que será posto no lugar do conteúdo atual da pilha
        '''
        try:
            self.__dados[posicao-1] = conteudo
        except IndexError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')

    def empilha(self, conteudo:any):
        '''Método que empilha cada elemento indicado para empilhar
        
        Argumentos:
        
        conteudo: valor que será empilhado. Caso seja uma lista de elementos, usa-se laço (estrutura de repetição).
        '''
        self.__dados.append(conteudo)

    def desempilha(self)->any:
        '''Método que desempilha cada elemento que estiver pertencente a tal pilha'''
        if self.estaVazia():
            raise PilhaException(f'Pilha vazia.')
        return self.__dados.pop()

    def __str__(self):
        s = ''
        for e in self.__dados:
            s+=f'{e} '
        return s

    def esvazia(self):
        '''Método que esvazia completamente uma pilha referenciada'''
        self.__dados.clear()