from modelos.pessoa import Pessoa

class Entregador(Pessoa):
    def __init__(self, nom, cpf, veic, cnh):
        super().__init__(nom, cpf)
        self.__veic = veic
        self.__cnh = cnh

    @property
    def veic(self):
        return self.__veic

    @property
    def cnh(self):
        return self.__cnh
