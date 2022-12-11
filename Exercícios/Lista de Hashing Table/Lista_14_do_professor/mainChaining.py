from ChainingHashTable import ChainingHashTable

# ------------------------------------------------ #
#  Programa Principal 
# ------------------------------------------------ #
size = int(input("Informe o tamanho da tabela hash desejada: "))
cht = ChainingHashTable(size)

# Armazenando elementos na tabela Hash
cht.put(12,'alex')
cht.displayTable()
input()

# Aqui, tenta-se inserir a mesma chave. Como a chave já existe, atualiza o valor
cht.put(12,'alex sandro')
cht.displayTable()
input()

cht.put(31,'nathan')
cht.displayTable()
input()

cht.put(90,'alice')
cht.displayTable()
input()

cht.put(28,'matheus')
cht.displayTable()
input()

cht.put(88,'duda')
cht.displayTable()
input()

cht.put(40,'naty')
cht.displayTable()
input()

cht.put(77,'alessandra')
cht.displayTable()
input()

cht.put(26,'dan')
cht.displayTable()
input()

cht.put(17,'jessika')
cht.displayTable()
input()


# A chamada ao método get() gera uma exceção se a chave não existir.
#print('get():', cht.get(111))

cht.remove(12)
cht.displayTable()

# A chamada ao método remove() gera uma exceção se a chave não existir.
#cht.get(111)