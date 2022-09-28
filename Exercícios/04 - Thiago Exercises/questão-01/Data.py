#27/09/2022
class Data:
    
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def getDia(self, novoDia: int):
        self.__dia = novoDia
    
    def getMes(self, novoMes: int):
        self.__mes = novoMes

    def getAno(self, novoAno: int):
        self.__ano = novoAno

    def __str__(self):
        if self.__mes > 9:
            return f"Hoje é {self.__dia}/{self.__mes}/{self.__ano}"
        else:
            self.__mes = self