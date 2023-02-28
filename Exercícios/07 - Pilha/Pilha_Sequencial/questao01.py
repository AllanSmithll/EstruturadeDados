# 16/01/2022
'''
Exercício para utilizar as operações de uma Pilha

- Exercício modificado por Allan Amâncio. Github: https://github.com/AllanSmithll
- Copiado de Yago César. Fiz apenas inverter()
'''

from PilhaSequencial import *
from time import sleep

choice = str()
element = str()
stackList = [Pilha()]

while choice != 'sair':

    stackIndex = 0
    selectedStack = stackList[stackIndex]
    print(
        f'''
        \rEditor de Pilha v1.2
        \r=====================================
        \rPilha selecionada: {stackIndex + 1} de {len(stackList)}
        \r[{selectedStack.topo() if not selectedStack.estaVazia() else ' '}] <- topo
        \r=====================================
        \r(e) Empilhar
        \r(d) Desempilhar
        \r(t) Tamanho
        \r(o) Obter elemento do topo
        \r(h) Mostrar como está a Pilha atual
        \r(v) Teste de pilha vazia
        \r(r) Criar nova Pilha
        \r(n) Inverter os elementos da pilha
        \r(z) Esvaziar a pilha
        \r(i) Inverter string (cancelado)
        \r(c) Concatenar duas pilhas (funciona com Pilha Encadeada)
        \r(m) Escolher outra pilha (cancelado)
        \r(b) Conversão dec/bin do topo (cancelado por funcionar apenas com números inteiros)
        \r(s) Sair
        \r=====================================
        '''
    )
    choice = input('Digite a sua opção > ').lower()

    if choice == 'e':
        element = input('\nElemento a ser empilhado > ')
        selectedStack.empilha(element)

    elif choice == 'd':
        try:
            print('\nValor removido da pilha:', selectedStack.desempilha())
        except PilhaException as pe:
            print('\nErro:', pe)

    elif choice == 't':
        print('\nTamanho da pilha:', len(selectedStack))

    elif choice == 'o':
        try:
            print('\nElemento do topo:', selectedStack.topo())
        except PilhaException as pe:
            print('\nErro:', pe)

    elif choice == 'h':
        if len(selectedStack) < 0:
            print("Pilha vazia!")
        else:
            print(f"A pilha selecionada está assim:")
            selectedStack.imprime()

    elif choice == 'v':
        if selectedStack.estaVazia():
            print('\nPilha vazia')
        else:
            print('\nHá pelo menos um elemento nesta pilha.')

    elif choice == 'r':
        stackList.append(Pilha())
        print('\nNova pilha adicionada com sucesso!')

    elif choice == 'z':
        if not selectedStack.estaVazia():
            selectedStack.esvazia()
        else:
            print('\nErro: não é possível esvaziar uma pilha que já está vazia.')
    
    elif choice == 'n':
        if (selectedStack.estaVazia()):
            print("Não é possível rotacionar uma pilha vazia.")
        selectedStack.inverte()

