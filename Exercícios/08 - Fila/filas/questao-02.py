# 08/05/2023
class Paciente:
    def __init__(self, nome, cpf, plano_saude):
        self.nome = nome
        self.cpf = cpf
        self.plano_saude = plano_saude

class FilaAtendimento:
    def __init__(self):
        self.pacientes = []

    def incluir_paciente(self):
        nome = input("Digite o nome do paciente: ")
        cpf = input("Digite o CPF do paciente: ")
        plano_saude = input("Digite o plano de saúde do paciente (ou 'Nenhum' caso não tenha): ")
        paciente = Paciente(nome, cpf, plano_saude)
        self.pacientes.append(paciente)
        print(f"Paciente {paciente.nome} adicionado ao sistema. Sua ordem de atendimento é {len(self.pacientes)}.")

    def realizar_chamada(self):
        if not self.pacientes:
            print("Não há pacientes aguardando atendimento.")
        else:
            paciente = self.pacientes.pop(0)
            print(f"Atendimento do paciente {paciente.nome} realizado.")

    def consultar_posicao_atual(self):
        if not self.pacientes:
            print("Não há pacientes aguardando atendimento.")
        else:
            print(f"O próximo paciente a ser atendido é {self.pacientes[0].nome}.")

    def listar_quantidade_atendidos(self):
        quantidade_atendidos = len(self.pacientes)
        print(f"{quantidade_atendidos} pacientes foram atendidos até o momento.")

fila_atendimento = FilaAtendimento()

while True:
    print("""
    Clinica Medica - Atendimento
    =============
    1. Incluir paciente
    2. Realizar chamada
    3. Consultar a posição atual
    4. Listar a quantidade de pacientes atendidos
    5. Sair
    """)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        fila_atendimento.incluir_paciente()
    elif opcao == 2:
        fila_atendimento.realizar_chamada()
    elif opcao == 3:
        fila_atendimento.consultar_posicao_atual()
    elif opcao == 4:
        fila_atendimento.listar_quantidade_atendidos()
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")
