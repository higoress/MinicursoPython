class Pessoa:

    __nome = str()
    __telefone = str()

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def dados(self):
        print("Nome:",self.__nome, "/Telefone:", self.__telefone)




