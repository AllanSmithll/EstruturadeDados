class Aluno:
    def __init__(self, matricula: int, nome: str, notas: list):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas

    def getnome(self):
        return self.__nome
    
    def getmatricula(self):
        return f"{self.__matricula}"

    def Media(self):
        s = 0
        for i in self.__notas:
            s += i

        media = s / len(self.__notas)
        return media

    def set_nome(self, novoNome):
        self.__nome = novoNome
        return self.__nome

    def addNota(self, novasNotas: float):
        novasNotas = []
        quantas = int(input("Quantas notas: "))
        for i in range(quantas):
            notas = float(input("Nota: "))
            novasNotas.append(notas)
        return novasNotas

    def __str__(self):
        return f"{self.__matricula};\n Nome: {self.__nome};\n {self.__notas}"
