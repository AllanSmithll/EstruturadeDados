from Pais import Pais

p1 = Pais("Brasil", "Brasilia", "8000000")
p2 = Pais("Russia", "Moscou", "17000000")

print(p1)
print(p2)

p1.addPaisDeFronteira("Uruguai")

print(p1.vizinhos)