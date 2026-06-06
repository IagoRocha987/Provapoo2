class Pessoa:
    def __init__(self, nom, cpf):
        self.__nom = nom
        self.__cpf = cpf

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, val):
        self.__nom = val

    @property
    def cpf(self):
        return self.__cpf
