from PilhaSequencial import Pilha

if __name__ == '__main__':
    numeros = []
    p1 = Pilha()
    print("A pilha é esta:", p1,)
    print(f'''\nEditor de Pilha do Allan Alves Amancio v1.0\n============================================================\n
    Pilha Selecionada: [{p1}]
    topo: {p1[:-1:]}
    ''')