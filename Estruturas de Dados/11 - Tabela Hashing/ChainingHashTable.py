
class AbsentKeyException(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class Entry:
    """Uma classe privada utilizada para encapsular os pares chave/valor"""
    __slots__ = ( "key", "value" )
    def __init__( self, entryKey, entryValue ):
        self.key = entryKey
        self.value = entryValue
        
    def __str__( self ):
        return "(" + str( self.key ) + ", " + str( self.value ) + ")"
 
class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        # inicializa a tabela de dispersão com todos os elementos iguais a um
        # list vazio
        self.table = list([] for i in range(self.size))


    def hash(self, key):
        ''' Método que retorna a posição na tabela hashing conforme a chave.
            Aplicação do cálculo do hash modular
        '''
        return key % self.size

    def put(self, key, data):
        '''
        Adiciona um par chave/valor à tabela hash
        '''
        slot = self.hash(key)
        print(f'key {key} mapeada ao slot {slot}')

        for entry in self.table[slot]:
            if key == entry.key:
                entry.value = data
                return slot
            
        self.table[slot].append(Entry(key,data))
        return slot
            

    def get(self, key):
        '''
        Obtem o valor armazenado na entrada referente à chave "key"
        '''
        slot = self.hash(key)
        #print(f'key {key} at slot {slot}')
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                return self.table[slot][i].value
        else:
            raise AbsentKeyException(f'Chave {key} inexistente na tabela hash')

   
    def __str__(self):
        info = ""
        for items in self.table:
            # examina se o slot da tabela hash tem um list com elementos
            if items == None:
                continue
            for entry in items:
                info += str(entry)
        return info

    def __len__(self):
        count = 0
        for i in self.table:
            count += len(i)
        return count
         

 
    def keys(self):
        """Retorna uma lista com as chaves armazenadas na hashTable.
        """
        result = []
        for lst in self.table:
            if lst != None:
                for entry in lst:
                    result.append( entry.key )
        return result

    def contains( self, key ):
        """Return True se somente se a tabela hash tem uma entrada com a chave passada
           como argumento.
        """
        entry = self.__locate( key )
        return isinstance( entry, Entry )


    def __locate(self, key):
        '''
        Método que verifica se uma chave está presente na tabela hash e devolve a
        entrada correspondente quando a busca é realizada com sucesso
        '''
        slot = self.hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                return self.table[slot][i]
        else:
            return None
          
    def remove(self, key):
        '''
        Método que remove a entrada correspondente à chave passada como argumento
        '''
        slot = self.hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                entry = self.table[slot][i]
                del self.table[slot][i]
                return entry
        raise AbsentKeyException(f'Chave {key} não está presente na tabela hash') 


    def displayTable(self):
        entrada = -1
        for items in self.table:
            entrada += 1
            print(f'Entrada {entrada:2d}: ', end='') 
            if len(items) == 0:
                print(' None')
                continue
            for entry in items:
                print(f'[ {entry.key},{entry.value} ] ',end='')
            print()

       

            
           
# ------------------------------------------------ #
#  Programa Principal 
# ------------------------------------------------ #
size = int(input("Informe o tamanho da tabela hash desejada: "))
cht1 = ChainingHashTable(size)


# Armazenando elementos na tabela Hash
cht1.put(12,'alex')
cht1.displayTable()
input()

# Aqui, tenta-se inserir a mesma chave. Como a chave já existe, atualiza o valor
cht1.put(12,'alex sandro')
cht1.displayTable()
input()

cht1.put(31,'nathan')
cht1.displayTable()
input()

cht1.put(90,'alice')
cht1.displayTable()
input()

cht1.put(28,'matheus')
cht1.displayTable()
input()

cht1.put(88,'duda')
cht1.displayTable()
input()

cht1.put(40,'naty')
cht1.displayTable()
input()

cht1.put(77,'alessandra')
cht1.displayTable()
input()

cht1.put(26,'dan')
cht1.displayTable()
input()

cht1.put(17,'jessika')
cht1.displayTable()
input()

# A chamada ao método get() gera uma exceção se a chave não existir.
#print('get():', cht1.get(111))

cht1.remove(12)
cht1.displayTable()

# A chamada ao método remove() gera uma exceção se a chave não existir.
#cht1.get(111)

 

''' 
# printing position of elements
print("The position of element 31 is : " + str(table1.search(31)))
print("The position of element 28 is : " + str(table1.search(28)))
print("The position of element 90 is : " + str(table1.search(90)))
print("The position of element 77 is : " + str(table1.search(77)))
print("The position of element 1 is : " + str(table1.search(1)))
print("\nTotal number of comaprisons done for searching = " + str(table1.comparisons))
print()
 
table1.remove(90)
table1.remove(12)
 
table1.display()


       
    
     # method that searches for an element in the table
    # returns position of element if found
    # else returns False
    def search(self, element):
        found = False
        position = self.h1(element)
        self.comparisons += 1
       
        if(self.table[position] == element):
            return position
       
        # if element is not found at position returned hash function
        # then we search element using double hashing
        else:
            limit = 50
            i = 2
            newPosition = position
            # start a loop to find the position
            while i <= limit:
                # calculate new position by double Hashing
                position = (i*self.h1(element) + self.h2(element)) % self.size
                self.comparisons += 1
                # if element at newPosition is equal to the required element
               
               
                if self.table[position] == element:
               
                    found = True
                    break
               
                elif self.table[position] == 0:
                    found = False
                    break
                   
                else:
                    # as the position is not empty increase i
                    i += 1
            if found:
                return position
            else:
                print("Element not Found")
                return found
'''
 
 
