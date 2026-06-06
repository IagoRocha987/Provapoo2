class Pedido:
    def __init__(self, cod, cli, peso, dist, tipo, fre):
        self.__cod = cod
        self.__cli = cli
        self.__peso = peso
        self.__dist = dist
        self.__tipo = tipo
        self.__fre = fre
        self.__stat = "Em preparação"

    @property
    def cod(self):
        return self.__cod

    @property
    def cli(self):
        return self.__cli

    @property
    def peso(self):
        return self.__peso

    @property
    def dist(self):
        return self.__dist

    @property
    def tipo(self):
        return self.__tipo

    @property
    def fre(self):
        return self.__fre

    @property
    def stat(self):
        return self.__stat

    @stat.setter
    def stat(self, val):
        self.__stat = val
