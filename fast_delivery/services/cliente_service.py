from modelos.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.__clis = []

    def add(self, nom, cpf, tel, end):
        cli = Cliente(nom, cpf, tel, end)
        self.__clis.append(cli)
        return cli

    def get(self, cpf):
        for cli in self.__clis:
            if cli.cpf == cpf:
                return cli
        return None

    def ver(self):
        return self.__clis
