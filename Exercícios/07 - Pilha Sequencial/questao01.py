from PilhaSequencial import Pilha

p1 = Pilha()

print(f'''Editor de Pilha do Allan Amancio
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

opcao = input("Digite sua opção")

p1 = p1.empilha(20)
print(p1)