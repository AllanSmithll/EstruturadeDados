# 06/01/2022
from PilhaSequencial import Pilha
from time import sleep

p1 = Pilha()

while True:
    print()
    sleep(1.5)
    print(f'''Editor de Pilha do Allan Amâncio (com números)
    {"="*35}
    Pilha Selecionada: {p1}
    [] <- topo
    {"="*35}
    (e) - Empilhar
    (d) - Desempilhar
    (t) - Tamanho
    (o) - Obter elemento do topo
    (v) - Teste de pilha vazia
    (r) - Criar nova Pilha
    (z) - Esvaziar
    (c) - Concatenar duas pilhas
    (m) - Escolher outra pilha
    (n) - Conversão dec/bin
    (s) - Sair
    {"="*35}''')

    # Selecionar e executar a opção
    opcao = input("Digite sua opção: ").lower()
    if opcao == 'e':
        valor = float(input("Digite um valor para empilhar: "))
        p1.empilha(valor)
        print(f"Valor {valor} adicionado à pilha com sucesso.")
        continue
    if opcao == 'd':
        p1.desempilha()
        print("Último elemento desempilhado.")
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
        pass



    '''
    EXERCÍCIO INCOMPLETO AINDA
    '''