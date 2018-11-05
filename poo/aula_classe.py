#   Exemplo de definição de uma classe em python
#   Notação CamelCase

class Cachorro:
    pass


#   A diretiva pass, permite que você crie uma definição sem implementá-la.
# Porque, caso você não implemente, isso gera erros.



#   Para atribuir características a uma classe (atributos)
#   __init__()
#   Para instanciar uma classe, ou seja, atribuir valores ao molde, se usa o
# metódo __init__(). Metódo é sinônimo de função
#   Você passa como parametro para o método init, as características (atributos)
# que você considera importante para ter em uma classe. No caso de cachorro,
# teremos nome e a idade.

class Cachorro:

    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

#   O primeiro argumento do método init, é uma refêrencia para os dados da
# classe. Desta maneira, a linguagem de programação sabe que você está referen-
# ciando a variavel da classe, e não a que você recebeu como parâmetro.
#   Historicamente, a variavel self, é usada para se referir a si mesmo, no
# entanto, qualquer nome que você usar é válido.
#   O operador ponto (.) permite que você acesse os atributos e métodos daquela
# classe específica.
# Ex:

class Cachorro:

    def __init__(este_cachorro,nome,idade):
        este_cachorro.nome = nome
        este_cachorro.idade = idade


#   É importante perceber que, quando você cria uma classe, ela só passa a ter
# valores, quando você cria um objeto (instancia uma classe).
#   No entanto, é possível, criar alguns atributos para a classe, ao invés de
# criar para o objeto. Desta maneira, todos os objetos pertencentes a aquela
# classe, possuirão o mesmo valor para aquele atributo.
# Ex:

class Cachorro:

    especie = "mamífero"

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    

#               CRIANDO OUTROS MÉTODOS
#   Assim como no método init, todos os outros métodos começam com uma variavel
# self, ou algo que o valha. Desta maneira, você consegue referenciar os dados
# da classe.
# Ex:

class Cachorro:

    especie = "mamífero"

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def imprimeDados(self):
        print("Dados do cachorro -> Nome:", self.nome, "/Idade:", self.idade)

    def latir(self):
        print("latido padrão: Au!Au!Au!")

# Mesmo que você não use o self, ele precisa ser um argumento do seu método.

        

#               HERANÇA
#   O conceito de herança em POO, significa que uma classe filha, herde
# características da classe pai. Os atributos e os metódos.
# No entanto, a classe filha pode sobescrever o funcionamento de alguns metódos
# da classe pai, e acrecentar alguns atributos



class Pinscher(Cachorro):

    def __init__(self,nome,idade):
        Cachorro.__init__(self,nome,idade)
        self.raca = "pinscher"


    def latir(self):
        print("latido pinscher: Grrr!Au!Grrr!Au!")



#           HERANÇA MULTIPLA
#   Em linguagens Orientadas a Objeto, uma classe filha pode herdar atributos
# de mais de uma classe pai. Para fazer essa henrança multipla basta colocar
# como parâmetro da classe as várias classes da qual ela herda.

class Dobermann(Cachorro):

    def __init__(self,nome,idade):
        Cachorro.__init__(self,nome,idade)
        self.tipo = "Dobermann"
        
    def latir(self):
        print("latir dobermann: AUAUAU")


class ViraLata(Dobermann,Pinscher):

    def latir(self):
        Pinscher.latir(self)














