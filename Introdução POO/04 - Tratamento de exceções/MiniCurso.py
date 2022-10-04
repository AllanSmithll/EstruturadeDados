# 03/10/2022
# Criarei uma aubclasse que herde de uma das exceções do topo da hierarquia Python de Exception

# Minha classe Exception para saber se o curso está esgotado

class CursoEsgotadoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

try:
    curso = []
    for i in range(20):    # Percorrerá por um intervalo de 20 elementos
        nome = input("Interessado: ")   # Receberá os nomes
        if (len(curso) == 15):   # Se o tamanho de curso for = 15, lançará a mensagem "Vagas esgotadas"
            raise CursoEsgotadoException("Vagas esgotadas.")
        curso.append(nome)  # Caso não chegue a 15 nomes, simplesmente curso = nome. Ou seja, a lista curso vai receber o nome que a variável "nome" receber do teclado
except CursoEsgotadoException as cee:
    print(cee)