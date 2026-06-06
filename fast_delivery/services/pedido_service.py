from modelos.pedido import Pedido
from modelos.entrega import EntregaComum, EntregaExpressa, EntregaPremium

class PedidoService:
    def __init__(self):
        self.__peds = []

    def add(self, cod, cli, peso, dist, tipo):
        if tipo == "1":
            entg = EntregaComum(dist)
            t_str = "Comum"
        elif tipo == "2":
            entg = EntregaExpressa(dist)
            t_str = "Expressa"
        else:
            entg = EntregaPremium(dist)
            t_str = "Premium"
        
        fre = entg.calcular_frete()
        ped = Pedido(cod, cli, peso, dist, t_str, fre)
        self.__peds.append(ped)
        return ped

    def get(self, cod):
        for ped in self.__peds:
            if ped.cod == cod:
                return ped
        return None

    def ver(self):
        return self.__peds
