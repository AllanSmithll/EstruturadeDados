class Cliente:
    def __init__(self, nome):
        self.nome = nome

class FilaAtendimento:
    def __init__(self):
        self.clientes_fila_pedido = []
        self.clientes_fila_pagamento = []
        self.clientes_fila_entrega = []

    def inserir_cliente_fila_pedido(self):
        nome = input("Digite o nome do cliente: ")
        cliente = Cliente(nome)
        self.clientes_fila_pedido.append(cliente)
        print(f"Cliente {cliente.nome} adicionado à fila de pedidos.")

    def remover_cliente_fila_pedido(self):
        if not self.clientes_fila_pedido:
            print("Não há clientes na fila de pedidos.")
        else:
            cliente = self.clientes_fila_pedido.pop(0)
            self.clientes_fila_pagamento.append(cliente)
            print(f"Cliente {cliente.nome} removido da fila de pedidos e adicionado à fila de pagamento.")

    def remover_cliente_fila_pagamento(self):
        if not self.clientes_fila_pagamento:
            print("Não há clientes na fila de pagamento.")
        else:
            cliente = self.clientes_fila_pagamento.pop(0)
            self.clientes_fila_entrega.append(cliente)
            print(f"Cliente {cliente.nome} removido da fila de pagamento e adicionado à fila de entrega.")

    def remover_cliente_fila_entrega(self):
        if not self.clientes_fila_entrega:
            print("Não há clientes na fila de entrega.")
        else:
            cliente = self.clientes_fila_entrega.pop(0)
            print(f"Cliente {cliente.nome} removido da fila de entrega.")

fila_atendimento = FilaAtendimento()

while True:
    print("""
    Restaurante Rei do Mocotó - Atendimento
    =======================================
    1. Inserir cliente na fila de pedido
    2. Remover cliente da fila de pedido e adicionar à fila de pagamento
    3. Remover cliente da fila de pagamento e adicionar à fila de entrega
    4. Remover cliente da fila de entrega
    5. Sair
    """)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        fila_atendimento.inserir_cliente_fila_pedido()
    elif opcao == 2:
        fila_atendimento.remover_cliente_fila_pedido()
    elif opcao == 3:
        fila_atendimento.remover_cliente_fila_pagamento()
    elif opcao == 4:
        fila_atendimento.remover_cliente_fila_entrega()
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")
