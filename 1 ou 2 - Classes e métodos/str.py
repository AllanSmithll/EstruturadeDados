class Smartphone:
    def __init__(self, marca, modelo, preço):
        self.marca = marca
        self.modelo = modelo
        self.preço = preço
    def __str__(self):
        return f"Smartphone {self.__marca} modelo {self.modelo} que custa {self.preço} reais."

str1 = Smartphone('Xiaomi', 'Redmi 8', '800')
print(str1)
