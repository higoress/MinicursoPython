from exemplo8 import Pessoa

class PessoaFisica(Pessoa):
    cpf = ""
    def __init__(self,nome,telefone,cpf):
        super().__init__(nome,telefone)
        self.cpf = cpf






#sobescrever metodo dados








    #def dados(self):
     #   print("Nome:",self.nome,"/Telefone:",self.telefone,"/CPF:",self.cpf)