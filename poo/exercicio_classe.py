# Exercicios sobre classes em Python:

# 1 - Construa uma classe Pessoa seguindo o seguinte modelo:

class Pessoa:

    def __init__(self, nome, cpf):
        pass

    def quem_eu_sou(self):
        pass #deve imprimir na tela "Eu sou da classe Pessoa"


# Agora utilizando a classe pessoa, com herança, crie duas outras classes,
# a classe Cliente e a classe Funcionario. A classe Cliente deve possuir o
# método comprar, onde o ele recebe o que ele deseja comprar, e adiciona a
# uma variavel chamada lista_de_desejos, que é uma lista. Você deve fazer que
# o método quem_sou_eu imprima "Eu sou da classe Cliente".

# Para a classe Funcionario, ele deve ter um atributo a mais que a pessoa, que
# é o atributo salario. Você deve adicionar o atributo salário no construtor
# da classe (__init__). Além disso, ele deve ter um método chamado trabalhar,
# que é similar ao método comprar da classe Cliente, no entanto, você deve
# adicionar a lista_de_desejos os locais onde o Funcionário deseja trabalhar.
# Você deve também, fazer que o método quem_sou_eu imprima "Eu sou da classe
# Funcionario"






# 2 - crie em um outro script uma classe chamada ControladorArquivo,
# onde você passará um nome
# de um arquivo como parâmetro, e salvar em uma variavel arquivo 
# Caso não seja passado, deve salvar um arquivo padrão, chamado "deposito.txt".
# Depois você deve criar dois métodos, um para ler, e outro para escrever no
# arquivo. Neste contexto trabalharemos com clientes, no entanto, você pode
# usar para ler e escrever outras coisas (por exemplo,usar no trabalho #DICABOA)
# o método escreve cliente, recebe como parâmetro, nome, e cpf. Ai escreve no
# arquivo usando append. Para não perder os dados escritos anteriormente.
# Você deverá escrever um cliente por linha no arquivo, respeitando
# a seguinte ordem, cpf + nome. No entanto, uma técnica usada para recuperar
# esses dados depois, é inserir entre as variaveis caracteres de controle.
# Por exemplo, vou escrever o cpf = 12345, e o nome = Joaquim. Eu insiro um
# caractere que geralmente não é usado no nome e no cpf, para quando for
# recuperar, poder usar o método split. Então ficaria assim:
# cpf + '/' + nome + '\n'
# e no arquivo, estaria assim : 12345/Joaquim
# Desta maneira, quando eu ler a linha, eu dou split('/') e tenho os dois
# valores que eu quero.
# A função de escrita ainda deve imprimir, "registrado com sucesso", caso
# seja escrito no arquivo com sucesso.
# A função de leitura, recebe um cpf como parâmetro, e deve retornar um objeto
# do tipo cliente. Então, ele recebe o cpf, e lê o arquivo linha por linha
# comparando com os cpf's escritos no arquivo. Caso ele chegue no final do
# arquivo, e não tenha encontado o cpf, ele imprime na tela "erro, cliente não
# existe", e retorna um null.

class Controlador_arquivo:

    def __init__(self,file="deposito.txt"):
        self.arquivo = file


    def escreve_cliente(self,nome,cpf):
        #with open(self.aquivo, "a") as controlador:
        pass # implementar o método conforme especificado

    def le_cliente(self,cpf):

        #with open(self.arquivo, "r") as controlador:
        
        pass # implementar o método conforme especificado

        #se sucesso, return Cliente(self,nome,cpf)

        #se fracasso, print("erro,...") dps return None









