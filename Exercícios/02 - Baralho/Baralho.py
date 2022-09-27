from Carta import Carta
import random

class Baralho:
    def __init__(self, embaralhar: bool = False):
        self.container = list()
        naipe = ["ouro", "espada", "copa", "paus"]
        cor = ["vermelho", "preto", "vermelho", "preto"]
        valor = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]
        for n in range(len(naipe)):
            for v in range(len(valor)):
                self.container.append(Carta(valor[v], naipe[n], cor[n]))
            
            if embaralhar:
                self.embaralhar()

    def __str__(self):
        s = ""
        for carta in self.container:
            s += (carta.__str__() + "\n")
        return s
    
    def __len__(self):
        return len(self.container)

    def embaralhar(self):
        random.shuffle(self.container)
    
    def retirarCarta(self) -> Carta:
        return self.container.pop()
    
    def temCarta(self) -> bool:
        if len(self.container) == 0:
            return False
        else:
            return True
    
    def receberCarta(self, carta: Carta):
        if carta not in self.container:
            self.container.append(carta)
            return True
        return False

    def juntarBaralho(self, outroBaralho):
        for i in range(len(outroBaralho)):
            carta_retirada = outroBaralho.retirarCarta()
            if not self.receberCarta(carta_retirada):
                outroBaralho.retirar.receberCarta(carta_retirada)
