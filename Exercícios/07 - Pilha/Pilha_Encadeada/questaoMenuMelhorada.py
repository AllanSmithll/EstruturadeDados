# 18/01/2023
'''
Exerício feito pelo colega Yago César, que trabalha na Assert-IFPB enquanto registro este código
'''
from PilhaEncadeada import Pilha, PilhaException

userChoice = str()
userInput = str()
element = str()
allStacks = [Pilha()]

while userChoice != 'sair':

    stackIndex = 0
    selectedStack = allStacks[stackIndex]
    """
    print(
        f'''
        \rEditor de Pilha v1.2
        \r=====================================
        \rPilha selecionada: {stackIndex + 1} de {len(allStacks)}
        \r[{selectedStack.topo() if not selectedStack.estaVazia() else ' '}] <- topo
        \r=====================================
        \r(e) Empilhar
        \r(d) Desempilhar
        \r(t) Tamanho
        \r(o) Obter elemento do topo
        \r(v) Teste de pilha vazia
        \r(r) Criar nova Pilha
        \r(n) Inverter os elementos da pilha
        \r(z) Esvaziar a pilha
        \r(c) Concatenar duas pilhas
        \r(m) Escolher outra pilha
        \r(n) Conversão dec/bin
        \r(s) Sair
        \r=====================================
        '''
    )"""
    userChoice = input('Digite a sua opção > ').lower()

    if userChoice == 'e':
        element = input('\nElemento a ser empilhado > ')
        selectedStack.empilha(element)

    elif userChoice == 'd':
        try:
            print('\nValor removido da pilha:', selectedStack.desempilha())
        except PilhaException as pe:
            print('\nErro:', pe)

    elif userChoice == 't':
        print('\nTamanho da pilha:', len(selectedStack))

    elif userChoice == 'o':
        try:
            print('\nElemento do topo:', selectedStack.topo())
        except PilhaException as pe:
            print('\nErro:', pe)

    elif userChoice == 'v':
        if selectedStack.estaVazia():
            print('\nPilha vazia')
        else:
            print('\nHá pelo menos um elemento nesta pilha.')

    elif userChoice == 'r':
        allStacks.append(Pilha())
        print('\nNova pilha adicionada com sucesso!')

    elif userChoice == 'i':
        pass

    elif userChoice == 'z':
        if not selectedStack.estaVazia():
            selectedStack.esvazia()
        else:
            print('\nErro: não é possível esvaziar uma pilha que já está vazia.')