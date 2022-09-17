class Bilhete:
    def __init__(self, id):
        self.id= id
        self.texto = ''
        print(self.id, 'Bilhete em branco criado')
    
    def addWord(self, word): #Público
        self.texto += word   #Público

    def __printText(self):   #Privado
        print(self.texto)    #Privado

recado = Bilhete(1)
recado.addWord('Prezado professor')
recado.__printText    #É privado, então não pode ser acessado por referência ao método
