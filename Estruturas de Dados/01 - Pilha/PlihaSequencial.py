# 23/10/2022
class PilhaSequencial:
    def __init__(self):
        self.__dados = [] # É essencialmente uma lista de dados

    def vazia(self) -> bool:
        return len(self.__dados) == 0  
        # Verifica se a Pilha está vazia. Ou seja, se a quantidade de elementos da Pilha é igual a 0.
    
    def tamanho(self) -> int:
        return len(self.__dados)

    def topo(self) -> int:
        return len(self.__dados[0])



# Programa principal

if __name__ == "__main__":
    pilha = PilhaSequencial()
    pilha.vazia()
    pilha.tamanho()
    print(pilha.dados)