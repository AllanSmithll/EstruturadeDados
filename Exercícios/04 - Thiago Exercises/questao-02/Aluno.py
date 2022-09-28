class Aluno:
    def __init__(self, matricula: int, nome: str, notas: list):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas

    def getnome(self):
        return self.__nome
    
#    def getmatricula(self):
