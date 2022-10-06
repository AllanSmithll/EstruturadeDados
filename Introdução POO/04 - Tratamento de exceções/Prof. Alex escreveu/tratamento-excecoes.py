def lerConteudo( fileName):
    stream = open(fileName,'rt')
    linhas = stream.readlines()
    stream.close()
    return linhas

try:
    while(True):
        print('''
        (1) Erro de lógica de Programação
        (2) Erros de condição do ambiente de execução do software
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
    print("Por favor, digite um índice válido.")
except ValueError:
    print("Por favor, digite um valor inteiro.")
except:
    print("Não possível acessar as notas.")
        

print('\n###### Chegamos ao final do programa ########')