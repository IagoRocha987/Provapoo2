from interfaces.calculo_frete_interface import CalculoFreteInterface

class EntregaComum(CalculoFreteInterface):
    def __init__(self, dist):
        self.__dist = dist

    def calcular_frete(self):
        return self.__dist * 1.5

class EntregaExpressa(CalculoFreteInterface):
    def __init__(self, dist):
        self.__dist = dist

    def calcular_frete(self):
        return self.__dist * 3.0

class EntregaPremium(CalculoFreteInterface):
    def __init__(self, dist):
        self.__dist = dist

    def calcular_frete(self):
        return (self.__dist * 5.0) + 20.0
