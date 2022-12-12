from ChainingHashTable import ChainingHashTable
from Computador import Computador

# ------------------------------------------------ #
#  Programa Principal: Parte 1
# ------------------------------------------------ #
size = int(input("Informe o tamanho da tabela hash desejada: "))
# cht = ChainingHashTable(size)

# # Armazenando elementos na tabela Hash
# cht.put(12,'alex')
# cht.displayTable()
# input()

# # Aqui, tenta-se inserir a mesma chave. Como a chave já existe, atualiza o valor
# cht.put(12,'alex sandro')
# cht.displayTable()
# input()

# cht.put(31,'nathan')
# cht.displayTable()
# input()

# print("Valor que tem chave 31: ", cht.get(31))
# input()

# cht.put(29, "Allan")
# cht.displayTable()
# input()

# cht.put(10, "Marcio")
# cht.displayTable()
# input()


# # A chamada ao método get() gera uma exceção se a chave não existir.
# #print('get():', cht.get(111))

# # A chamada ao método remove() gera uma exceção se a chave não existir.
# cht.remove(12)
# cht.displayTable()

# # A chamada de __len__() retorna a quantidade de pares chave/valor

# print("\nQuantos pares chave e valor há na Hash Table?", cht.__len__())

# ------------------------------------------------ #
#  Programa Principal: Parte 2
# ------------------------------------------------ #

ht = ChainingHashTable(size)
c1 = Computador('192.168.0.1', 'Intel i7 8GB RAM 1TB HD')
ht.put(c1, "Meu computador")
ht.displayTable()
print(ht.__str__())