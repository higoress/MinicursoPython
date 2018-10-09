# EXERCICIO 1:

# CRIE DUAS VARIAVEIS, A PRIMEIRA DELAS PARA ARMAZENAR OS DADOS DE UM CLIENTE: CPF, NOME, TELEFONE.
# OS DADOS DO CLIENTE DEVEM ESTAR CONTIDOS EM UMA VARIAVEL QUE PERMITA OS DADOS ESTAREM RELACIONADOS
# A SEGUNDA VARIAVEL DEVE CONTER OS DADOS DE TODOS OS CLIENTES QUE FOREM ADICIONADOS NO SISTEMA
# ADICIONE A PRIMEIRA VARIAVEL A SEGUNDA


cliente = ("12312312312", "Daniel San", "34 3236 7777")
clientes = []

clientes.append(cliente)


# FACA UMA FUNCAO QUE ADICIONE NOVOS CLIENTES A LISTA QUE VOCE CRIOU ANTES NO EXERCICIO 1
# APOS ADICIONAR IMPRIMA A MENSAGEM : "ADICIONADO COM SUCESSO!"
# FACA UMA FUNCAO QUE IMPRIMA A LISTA DE CLIENTES


def adiciona_cliente(cpf, nome, telefone):
    cliente = (cpf, nome, telefone)
    clientes.append(cliente)
    print("Adicionado com sucesso!")


def imprime_clientes():
    print(clientes)


# MODIFIQUE A FUNÇÃO QUE ADICIONA UM CLIENTE NA LISTA
# FACA UMA VERIFICACAO ANTES DE ADICIONAR, VEJA SE O CAMPO CPF RESPEITA A SEGUINTE CONDICAO:
# O CAMPO CPF DEVE CONTER APENAS NUMEROS, SE VERDADEIRO, ADICIONE
# CASO O CPF ESTEJA NO FORMATO ERRADO, IMPRIMA UMA MENSAGEM QUE NÃO FOI POSSIVEL ADICIONAR
# DICA: A FUNCAO NATIVA str POSSUI UMA OUTRA FUNCAO QUE VERIFICA SE OS CARACTERES DE UMA STRING SAO NUMERICOS


def nova_adiciona_cliente(cpf, nome, telefone):
    if (str.isnumeric(cpf)):
        cliente = (cpf, nome, telefone)
        clientes.append(cliente)
        print("Adicionado com sucesso!")
    else:
        print("CPF NO FORMATO ERRADO, tente com apenas números")


#   FACA QUATRO  NOVAS FUNCOES:
#   1 - REMOVER UM CLIENTE DA LISTA A PARTIR DO CPF
#   2 - BUSCAR OS DADOS DE UM CLIENTE NA LISTA A PARTIR DO NOME
#   3 - MODIFIQUE A FUNCAO IMPRIME PARA IMPRIMIR UM CLIENTE POR LINHA
#   4 - ATUALIZAR OS DADOS DE UM CLIENTE EXISTENTE (CONSIDERE QUE O CPF ESTA SEMPRE CORRETO)


def nova_imprime():
    print("Clientes:")
    for x in clientes:
        print("CPF:", x[0], "Nome:", x[1], "Telefone:", x[2])


def remove_cliente(cpf):
    for x in clientes:
        if x[0] == cpf:
            clientes.remove(x)
            print("Removido com sucesso")
            return

    print("Impossível remover, cpf não existe")


def busca_cliente(nome):
    for x in clientes:
        if x[1] == nome:
            print("Dados Cliente:", x)
            return

    print("Cliente não existe")


def atualiza_cliente(cpf, novo_nome, novo_telefone):
    i = 0
    while i < len(clientes):
        if clientes[i][0] == cpf:
            clientes[i] = (cpf, novo_nome, novo_telefone)
            print("Atualizado com sucesso")
            return
        i += 1
    print("Cliente não existe")

# TEMOS NOSSO PRIMEIRO CRUD (CREATE READ UPDATE DELETE)
# AGORA CRIAR UMA FUNÇÃO QUE FICA EM LOOP INFINITO, E QUE USE TODAS AS OUTRAS FUNCOES DO CRUD
