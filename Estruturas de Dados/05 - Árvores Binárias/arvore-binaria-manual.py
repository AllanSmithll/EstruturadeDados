# 20/10/2022
# Como fazer uma árvore binária da forma mais chata possível, com a versão Pré-ordem

class Node:
    def __init__(self,data:object):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    @property
    def data(self)->object:
        return self.__data

    @data.setter
    def data(self, newData:object):
        self.__data = newData

    @property
    def leftChild(self)->'Node':
        return self.__leftChild

    @leftChild.setter
    def leftChild(self, newLeftChild:object):
        self.__leftChild = newLeftChild

    @property
    def rightChild(self)->'Node':
        return self.__rightChild

    @rightChild.setter
    def rightChild(self, newRightChild:'Node'):
        self.__rightChild = newRightChild

    def insertLeft(self, data:object):
        if self.__leftChild == None:
            self.__leftChild = Node(data)	

    def insertRight(self,data:object):
        if self.__rightChild == None:
            self.__rightChild = Node(data)

    def __str__(self):
        return str(self.__data)

    def hasLeftChild(self)->bool:
        return self.__leftChild != None

    def hasRightChild(self)->bool:
        return self.__rightChild != None
        

# Funcao que realiza o percurso em preordem (não é um método da classe BinaryTree
def preorder(node):
    if( node == None):
        return
    print(f'{node.data} ',end='')
    preorder(node.leftChild)
    preorder(node.rightChild)

'''
             10
            .  .
           .    .
          .      .
         20      30
                .
               .
              15
                .
                 .
                 25
          
'''

raiz = Node(10)
raiz.insertLeft(20)
raiz.insertRight(30)

cursor = raiz.rightChild
cursor.insertLeft(15)

cursor = cursor.leftChild
cursor.insertRight(25)

preorder(raiz)