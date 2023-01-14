# 06123/01/2022
'''
Exercício para utilizar as operações de uma Pilha

- Exercício moficado por Allan Amâncio. Github: https://github.com/AllanSmithll
'''

from PilhaSequencial import *
from time import sleep

p1 = Pilha()

while True:
    print()
    sleep(1.5)
    print(f'''Editor de Pilha do Allan Amâncio (com números)
    {"="*35}
    Pilha atual: {p1}
    (e) - Empilhar
    (d) - Desempilhar
    (t) - Tamanho
    (o) - Obter elemento do topo
    (v) - Teste de pilha vazia
    (r) - Criar nova Pilha
    (z) - Esvaziar a pilha
    (n) - Conversão dec/bin
    (s) - Sair
    {"="*35}''')

   # Selecionar e executar a opção
    opcao = str(input("Digite sua opção: ")).lower()
    if opcao == 'e':
        try:
            valor = float(input("Digite um valor para empilhar: "))
        except ValueError:
            print("Valor inválido! Digite novamente, mas que seja um número real.")
            valor = float(input("Digite outro valor para empilhar: "))
        finally:
            p1.empilha(valor)
            print(f"Valor {valor} adicionado à pilha com sucesso.")
            continue

    if opcao == 'd':
        try:
            assert p1.estaVazia()
        except AssertionError:
            print("Pilha vazia! Não pode desempilhar.")
        else:
            p1.desempilha(valor)
            print("Último elemento desempilhado.")
            continue
    if opcao == 't':
        print(f"A pilha possui {p1.tamanho()} elemento(s).")
    if opcao == 'o':
        ultimo_elemento_pilha = p1.tamanho()
        topo = p1.elemento(ultimo_elemento_pilha)
        print(f"{topo} é o elemento do topo.")
    if opcao == "v":
        if p1.estaVazia(): print("Pilha vazia.")
        else: print(f"Pilha não está vazia. Tem {p1.tamanho()} elemento(s).")
    if opcao == "r":
        p2 = Pilha()
        print(f"Pilha criada com sucesso.")
    if opcao == 'z':
        Pilha.esvazia()
        print(f"Pilha {Pilha} esvaziada com sucesso.")
    if opcao == 'c':
        print(f"Concatenar com qual pilha? ")
        p1.concatena(p2)
    else:
        print("Opção inválida!")


    '''
    EXERCÍCIO INCOMPLETO AINDA
    '''