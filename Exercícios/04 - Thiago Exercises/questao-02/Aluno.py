class Aluno:
    def __init__(self, matricula: int, nome: str, notas: list):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas

    @property
    def getnome(self):
        return self.__nome
    
    @property
    def getmatricula(self):
        return self.__matricula

    @property
    def getNotas(self):
        return self.__notas

    def addNota(self, novaNota):
        if novaNota not in self.__notas:
            self.__notas.append(novaNota)
        

    def __str__(self):
        return f"{self.__matricula};\n Nome: {self.__nome};\n {self.__notas}"
