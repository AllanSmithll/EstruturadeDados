class Pais:
    def __init__(self, nome:str, capital:str, dimensao:int):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
    
    @property
    def getNome(self) -> str:
        return self.__nome

    @property
    def getCapital(self) -> str:
        return self.__capital

    @property
    def getDimensao(self) -> int:
        return self.__dimensao
    
    def vizinhos(self) -> list:
        return self.__vizinhos

    def addPaisDeFronteira(self, nome_do_pais:str):
        if nome_do_pais not in self.__vizinhos:
            self.__vizinhos.append(nome_do_pais)

    def __str__(self):
        return f'{self.__nome}, capital {self.__capital}, com {self.__dimensao} Km².'