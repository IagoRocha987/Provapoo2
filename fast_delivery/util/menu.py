import os

class Menu:
    @staticmethod
    def lim():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def show():
        print("\n--- FastDelivery Express ---")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Buscar Cliente")
        print("4 - Cadastrar Entregador")
        print("5 - Criar Pedido")
        print("6 - Listar Pedidos")
        print("7 - Atualizar Status do Pedido")
        print("0 - Sair")
