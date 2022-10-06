# 06/10/2022

def lerConteudo( fileName):
    stream = open(fileName,'rt')
    linhas = stream.readlines()  # Professor criou um método que lê um arquivo de texto, retorando as linhas desse tal arquivo
    stream.close()
    return linhas

try:
    while(True):
        print('''
        (1) Erro de lógica de Programação
        (2) Erros de condição do ambiente de execução do software  # Escolhendo a opção de erro
        (3) Erros graves que não permitem recuperação
        --------------------------------------------------''')
        opcao = int(input('opcao: '))

        if opcao == 1: # Erro tipo 1
            # limite de um array estourado
            notas = [5,10,7,8,6]
            print(notas)        
            index = int(input('Digite o índice de acesso ao array:'))
            print('Nota exibida:', notas[index])
        elif opcao == 2:
            # abrir um arquivo não encontrado
            arquivo = input('Informe o caminho e nome do arquivo: ')       
            print(lerConteudo(arquivo))
        
        elif opcao == 3:
            print('Não é interessante simular....')
            print('Exemplo: falta de memória, erro interno do interpretador, etc.')
        else:
            break

except IndexError:
    print("Por favor, digite um índice válido.")   # Se o índice for inválido
except ValueError:
    print("Por favor, digite um valor inteiro.")  # Se não digitar um número inteiro
except Exception as e:   
    print('Mensagem:', e)
    print("Classe da exceção:", e.__class__)   # Diz a classe da exceção(o tipo de exceção)
        

print('\n###### Chegamos ao final do programa ########')