from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.entrega_service import EntregaService
from util.menu import Menu
from util.formatador import Formatador

def main():
    s_cli = ClienteService()
    s_ped = PedidoService()
    s_ent = EntregaService()
    prox = 1001

    while True:
        Menu.show()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            Menu.lim()
            nom = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            tel = input("Telefone do cliente: ")
            end = input("Endereço do cliente: ")
            s_cli.add(nom, cpf, tel, end)
            print(f"Cliente {nom} cadastrado com sucesso!")

        elif opc == "2":
            Menu.lim()
            clis = s_cli.ver()
            if not clis:
                print("Nenhum cliente cadastrado.")
            for c in clis:
                print(f"Nome: {c.nom} | CPF: {c.cpf} | Tel: {c.tel} | End: {c.end}")

        elif opc == "3":
            Menu.lim()
            cpf = input("Digite o CPF para buscar: ")
            c = s_cli.get(cpf)
            if c:
                print(f"Cliente Encontrado -> Nome: {c.nom} | Tel: {c.tel} | End: {c.end}")
            else:
                print("Cliente não encontrado.")

        elif opc == "4":
            Menu.lim()
            nom = input("Nome do entregador: ")
            cpf = input("CPF do entregador: ")
            veic = input("Veículo: ")
            cnh = input("CNH: ")
            s_ent.add(nom, cpf, veic, cnh)
            print(f"Entregador {nom} cadastrado com sucesso!")

        elif opc == "5":
            Menu.lim()
            cpf = input("CPF do cliente do pedido: ")
            c = s_cli.get(cpf)
            if not c:
                print("Cliente não localizado! Cadastre o cliente antes de gerar o pedido.")
                continue
            
            try:
                peso = float(input("Peso do pedido (kg): "))
                dist = float(input("Distância da entrega (km): "))
                print("Tipos de Entrega: 1-Comum | 2-Expressa | 3-Premium")
                tipo = input("Escolha o tipo: ")
                
                if tipo not in ["1", "2", "3"]:
                    print("Tipo inválido de entrega.")
                    continue
                    
                ped = s_ped.add(prox, c, peso, dist, tipo)
                print(f"Pedido {prox} criado! Valor do Frete: {Formatador.mon(ped.fre)}")
                prox += 1
            except ValueError:
                print("Erro: digite valores numéricos válidos.")

        elif opc == "6":
            Menu.lim()
            peds = s_ped.ver()
            if not peds:
                print("Nenhum pedido registrado.")
            for p in peds:
                print(f"Cod: {p.cod} | Cliente: {p.cli.nom} | Tipo: {p.tipo} | Frete: {Formatador.mon(p.fre)} | Status: {p.stat}")

        elif opc == "7":
            Menu.lim()
            try:
                cod = int(input("Código do pedido: "))
                p = s_ped.get(cod)
                if p:
                    print(f"Status atual: {p.stat}")
                    print("1 - Em preparação\n2 - Saiu para entrega\n3 - Entregue\n4 - Cancelado")
                    nova = input("Escolha o novo status: ")
                    if nova == "1": p.stat = "Em preparação"
                    elif nova == "2": p.stat = "Saiu para entrega"
                    elif nova == "3": p.stat = "Entregue"
                    elif nova == "4": p.stat = "Cancelado"
                    else: print("Opção inválida.")
                    print(f"Status do pedido {cod} atualizado para: {p.stat}")
                else:
                    print("Pedido não encontrado.")
            except ValueError:
                print("Erro: digite um código válido.")

        elif opc == "0":
            print("Saindo do sistema FastDelivery...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
