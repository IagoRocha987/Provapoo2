from modelos.entregador import Entregador

class EntregaService:
    def __init__(self):
        self.__ents = []

    def add(self, nom, cpf, veic, cnh):
        ent = Entregador(nom, cpf, veic, cnh)
        self.__ents.append(ent)
        return ent

    def ver(self):
        return self.__ents
