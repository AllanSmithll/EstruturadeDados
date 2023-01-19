# Para testar comandos - 18/01/2023
from Pilha_Sequencial.PilhaSequencial import Pilha

if __name__ == '__main__':
    p1 = Pilha()
    p1.empilha(40)
    p1.empilha(30)
    p1.empilha(20)
    p1.empilha(10)
    p1.empilha("Tua mãe, aquela gostosa.")
    p1.imprime()