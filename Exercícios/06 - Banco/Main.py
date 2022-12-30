from Conta import Conta
from Banco import *

# BAB - Banco Allan Bank
bab = Banco()
bab.addConta(123, 'Alex')
bab.addConta(456, 'Clodoaldo')
bab.addConta(457, 'Yago')
bab.addConta(458, 'Márcio')
bab.addConta(120, 'Caio')
bab.addConta(121, 'Felipe')
bab.addConta(12, 'Allan')


print('''
    |--------------------------------------------------|
    | Banco Allan Bank, o banco de todos os paraibanos |
    |                                                  |
    |        Selecione alguma opção do Menu            |
    |                                                  |
    | 1 -> Saque                                       |
    | 2 -> Depósito                                    |
    | 3 -> Acessar conta                               |
    | 4 -> Sair                                        |
    |--------------------------------------------------|
''')
print()
opcao = int(input("Digite aqui sua opção: "))

try:
    continua = "SIM"
    while continua == "SIM":
        if opcao == 1:
            numero_conta = int(input("Número da conta: "))
            valor_saque = float(input("Valor do saque: "))
            bab.sacar(numero_conta, valor_saque)
            print(f"Valor sacado com sucesso da conta {numero_conta}.")
            continua = input("Precisa de algo? Sim ou não? ").upper()

            if continua == "SIM":
                opcao = int(input('\nDigite sua próxima opção ("4" para sair): '))
                continue
            else:
                break

        if opcao == 2:
            numero_conta = int(input("Número da conta: "))
            valor_deposito = float(input("Valor do depósito: "))
            bab.depositar(numero_conta, valor_deposito)
            print(f"Valor adicionado com sucesso da conta {numero_conta}.")
            continua = input("\nPrecisa de algo a mais? Sim ou não? ").upper()

            if continua == "SIM":
                opcao = int(input('Digite sua próxima opção ("4" para sair): '))
                continue
            else:
                break

        if opcao == 3:
            numero_conta = int(input("Número da conta: "))
            bab.acessarConta(numero_conta)
            continua = input("Precisa de algo? Sim ou não? ").upper()

            if continua == "SIM":
                opcao = int(input('\nDigite sua próxima opção ("4" para sair): '))
                continue
            else:
                break

        if opcao == 4:
            continua = "NÃO"
        

except OperacaoInvalidaException as oie:
    print(oie)

print("\nObrigado por acessar nosso sistema.")









