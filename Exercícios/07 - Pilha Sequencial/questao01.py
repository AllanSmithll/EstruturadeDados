# 06123/01/2022
'''
Exercício para utilizar as operações de uma Pilha

- Exercício moficado por Allan Amâncio. Github: https://github.com/AllanSmithll
'''

from PilhaSequencial import *
from time import sleep
from converterDecBin import converterDecimalBinary

p1 = Pilha()

while True:
    print()
    sleep(1.5)
    print(f'''Editor de Pilha do Allan Amâncio (com números inteiros)
    {"="*35}
    Pilha atual: {p1}
    (e) - Empilhar
    (d) - Desempilhar
    (t) - Tamanho
    (o) - Obter elemento do topo
    (v) - Teste de pilha vazia
    (r) - Criar nova Pilha
    (z) - Esvaziar a pilha
    (s) - Sair
    {"="*35}''')

   # Selecionar e executar a opção
    opcao = str(input("Digite sua opção: ")).lower()
    if opcao == 'e':
        try:
            valor = int(input("Digite um valor para empilhar: "))
        except ValueError:
            print("Valor inválido! Digite novamente, mas que seja um número real.")
            valor = int(input("Digite outro valor para empilhar: "))
        finally:
            p1.empilha(valor)
            print(f"Valor {valor} adicionado à pilha com sucesso.")
            continue

    if opcao == 'd':
        p1.desempilha()
        print("Último elemento desempilhado.")
        continue
    if opcao == 't':
        print(f"A pilha possui {p1.tamanho()} elemento(s).")
    if opcao == 'o':
        ultimo_elemento_pilha = p1.tamanho()
        topo = p1.elemento(ultimo_elemento_pilha)
        print(f"{topo} é o elemento do topo.")
        continue
    if opcao == "v":
        if p1.estaVazia(): print("Pilha vazia.")
        else: print(f"A pilha não está vazia. Tem {p1.tamanho()} elemento(s).")
        continue
    if opcao == "r":
        p2 = Pilha()
        print(f"Pilha criada com sucesso.")
        continue
    if opcao == 'z':
        p1.esvazia()
        print(f"Pilha esvaziada com sucesso.")
        continue
    # if opcao == 'n':
    #     for i in range(p1.tamanho()):
    #         ultimo = p1.desempilha()
    #         numConvertidoBin = print(converterDecimalBinary(ultimo))
    #         p1.empilha(numConvertidoBin)
    #     continue
    if opcao =='s':
        print("Até logo!")
        break
    else:
        print("Opção inválida!")