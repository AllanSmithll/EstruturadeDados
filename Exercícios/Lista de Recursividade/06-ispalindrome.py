# 16/10/2022
# Exercício de palíndromo usando recursividade

def ispalindrome(str) -> bool:
    formatada = str.lower().strip().replace(' ', '') # Formatando assim: deixando minúsculas as letras, tirando os espaços da direita e esquerda, e trocando os espaços pelo vazio
    if formatada == '':  # Se string formatada for vazia, return True, porque vazio é igual a vazio
        return True
    return True if ispalindrome(formatada[1:-1]) and formatada[0] == formatada[-1] else False
    '''
    Retorne True se a chamada da função do elemento da posição 1 até o último elemento da string e o elemento da posição 0 for igual a todos os elementos da string formatada do fim até o começo. Ou seja, se do começo ao fim é igual do fim até o começo. Isso que é um palíndromo. Caso contrário, não é um palíndromo
    '''

# Programa principal
print(ispalindrome("a sacada da casa"))