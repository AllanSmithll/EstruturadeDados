from No import No   # Importando a clase No

def preordem(no_inicial):
    if no_inicial is None:
        return
    print(f'{no_inicial.carga}', end=' ')
    preordem(no_inicial.esq)
    preordem(no_inicial.dir)

    '''
    Pré ordem:
        1- Primeiramente, vê se o nó raiz é None. Se for, retorna uma árvore vazia. Caso não, imprime a raiz e continua a percorrer a árvore.
        2- Depois, vai para a subárvore (filho da raiz) esquerda e imprime. Continua a percorrer, o lado esquerdo de cada subárvore (neto, bisneto da raiz) e imprime. Caso não tenha mais como precorrer pela esquerda, volta para o nó pai (o que estiver acima).
        3 - Por fim, percorre pelo filho direito de cada subárvore, imprimindo cada um dos elementos da direita.
        4 - Quando acabar os nós filhos e netos da subárvore esquerda da raiz, volta pra raiz r e faz o mesmo percurso, só que na subárvore direita da raiz.
    '''


def emordem(no_inicial):
    if no_inicial is None:
        return
    emordem(no_inicial.esq)
    print(f'{no_inicial.carga}', end=' ')
    emordem(no_inicial.dir)

    '''
    Em ordem:
        1- Começa da subárvore (filho da raiz) esquerda e imprime. Continua a percorrer, o lado esquerdo de cada subárvore (neto, bisneto da raiz) e imprime. Caso não tenha mais como precorrer pela esquerda, volta para o nó pai (o que estiver acima).
        1- Primeiramente, vê se o nó raiz é None. Se for, retorna uma árvore vazia. Caso não, imprime a raiz e continua a percorrer a árvore.
        2- Depois, vai para a subárvore (filho da raiz) esquerda e imprime. Continua a percorrer, o lado esquerdo de cada subárvore (neto, bisneto da raiz) e imprime. Caso não tenha mais como precorrer pela esquerda, volta para o nó pai (o que estiver acima).
        3 - Por fim, percorre pelo filho direito de cada subárvore, imprimindo cada um dos elementos da direita.
        4 - Quando acabar os nós filhos e netos da subárvore esquerda da raiz, volta pra raiz r e faz o mesmo percurso, só que na subárvore direita da raiz.
    '''


def posordem(no_inicial):
    if no_inicial is None:
        return
    posordem(no_inicial.esq)
    posordem(no_inicial.dir)
    print(f'{no_inicial.carga}', end=' ')


def busca(chave, no_inicial)->bool:
    if no_inicial is None:
        return False
    if no_inicial.carga == chave:
        return True
    if ( busca(chave, no_inicial.esq)):
        return True
    else:
        return busca(chave, no_inicial.dir)

raiz = No(10)
raiz.esq = No(32)
raiz.dir = No(23)
cursor = raiz.esq # cursor desce para o nó 32
cursor.esq = No(12)
cursor.dir = No(40)
cursor = cursor.esq
cursor.esq = No(5)
cursor = raiz.dir # cursor desce para o nó 23, a partir do raiz
cursor.dir = No(30)
cursor = cursor.dir # cursor desce para o nó 30
cursor.esq = No(60)
cursor = cursor.esq # cursor desce par ao nó 60
cursor.dir = No(22)

preordem(raiz)
print()
emordem(raiz)
print()
posordem(raiz)



