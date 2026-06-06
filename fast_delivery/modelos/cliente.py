from modelos.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nom, cpf, tel, end):
        super().__init__(nom, cpf)
        self.__tel = tel
        self.__end = end

    @property
    def tel(self):
        return self.__tel

    @property
    def end(self):
        return self.__end
