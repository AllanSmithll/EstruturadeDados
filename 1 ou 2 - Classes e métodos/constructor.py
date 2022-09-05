class Carro:
    def __init__(self, modelo='Wolks'):
        self.modelo = modelo

carro1 = Carro()
carro2 = Carro('Gol')
print(carro1.modelo)
print(carro2.modelo)
