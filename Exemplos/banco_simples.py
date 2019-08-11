###---------------------------------------------------------------------------------------------------------------//
###ALGC
###Sistema de cadastro para banco em listas -- Python --
###--------------------------------------------------------------------------------------------------------------//

Contas = {'cod' : [], 'saldo' : [], 'tr' : []}
Trans = {'cod' : [], 'tipo' : [], 'origem' : [], 'destino' : [], 'valor' : []}
Clientes = {'cod' : [], 'nome' : [], 'tel' : [], 'cc' : []}
numClientes = 0

ok = True
while ok:

    # Menu Inicio ---------------------------------------------------------------------------------------------//
    print ("")
    print ("1 - Cliente")
    print ("2 - Transaçao")
    print ("3 - Sair")

    menuop = input("Digite o numero da opçao desejada: ")

    # Fecha Programa -----------------------------------------------------------------------------------------//
    if menuop == '3':
        ok = False

    # Menu Cliente ------------------------------------------------------------------------------------------//
    if menuop == '1':

        ok1 = True
        while ok1:

            print("")
            print("1 - Inserir novo cliente")
            print("2 - Consultar dados de um cliente")
            print("3 - Atualizar cadastro de um cliente")
            print("4 - Remover um clientes")
            print("5 - Imprimir lista de clientes")
            print("6 - Voltar")

            menuCliente = input ("\nDigite o numero da opçao desejada: ")

            ## Sair do menu cliente ----------------------------------------------------------------------//
            if menuCliente == '6':
                ok1 = False

            ## 1 - Inserir novo cliente ------------------------------------------------------------------//
            if menuCliente == '1':

                if numClientes < 50:

                    cod = input ("\nInforme o codigo do cliente: ")
                    nome = input ("Informe o nome do cliente: ")
                    tel = input ("Informe o telefone do cliente: ")
                    cc = input ("Informe o numero da conta corrente do cliente: ")
                    pdeposito = input ("Informe o valor do deposito inicial: ")
                    pdeposito = float(pdeposito)

                    Clientes['cod'].append(cod)
                    Clientes['nome'].append(nome)
                    Clientes['tel'].append(tel)
                    Clientes['cc'].append(cc)
                    Contas['cod'].append(cc)
                    Contas['saldo'].append(pdeposito)


                    numClientes = numClientes + 1

                else:
                    print("\nNumero maximo de clientes atingido!!")

            ## 2 - Consultar dados de um cliente -------------------------------------------------------//
            if menuCliente == '2':

                consultar = input ("\nInforme o codigo do cliente: ")
                consultarV = consultar in Clientes['cod']

                if consultarV == True:

                    pos = Clientes['cod'].index(consultar)
                    print("Codigo \t Nome \t\t Telefone \t Conta")
                    print("{0} \t {1} \t {2} \t {3} \t {4}".format(Clientes['cod'][pos],Clientes['nome'][pos],Clientes['tel'][pos],Clientes['cc'][pos],Contas['saldo'][pos]))

                else:
                    print("Codigo invalido!!!")

            ## 3 - Atualizar cadastro de um cliente --------------------------------------------------//
            if menuCliente == '3':

                consultar = input ("\nInforme o codigo do cliente: ")
                consultarV = consultar in Clientes['cod']

                if consultarV == True:

                    #newcodigo = input ("\nInforme o novo codigo do cliente: ")
                    newnome = input ("Informe o novo nome do cliente: ")
                    newtel = input ("Informe o novo telefone do cliente: ")
                    #newcc = input ("Informe o novo numero da conta corrente do cliente: ")

                    pos = Clientes['cod'].index(consultar)

                    #Clientes['cod'][pos] = newcodigo
                    Clientes['nome'][pos] = newnome
                    Clientes['tel'][pos] = newtel
                    #Clientes['cc'][pos] = newcc

                    print("\nDados atualizados!!!\n")

                else:
                    print("Codigo invalido!!!")


            ## 4 - Remover um clientes -------------------------------------------------------------//
            if menuCliente == '4':

                consultar = input ("\nInforme o codigo do cliente: ")
                consultarV = consultar in Clientes['cod']

                if consultarV == True:

                    pos = Clientes['cod'].index(consultar)
                    Clientes['cod'].pop(pos)
                    Clientes['nome'].pop(pos)
                    Clientes['tel'].pop(pos)
                    Clientes['cc'].pop(pos)
                    Contas['cod'].pop(pos)
                    Contas['saldo'].pop(pos)

                    numClientes = numClientes - 1

                    print("Removido com sucesso")

                else:
                    print("Codigo invalido!!!")


            ## 5 - Imprimir lista de clientes -----------------------------------------------------//
            if menuCliente == '5':

                print("Codigo \t Nome \t\t Telefone \t Conta \t Saldo")
                print()

                for i in range(numClientes):

                    print("{0} \t {1} \t {2} \t {3} \t {4}".format(Clientes['cod'][i],Clientes['nome'][i],Clientes['tel'][i],Clientes['cc'][i], Contas['saldo'][i]))


    # FIM do Menu Cliente --------------------------------------------------------------------------//

    # Menu Transaçao -------------------------------------------------------------------------------//
    if menuop == '2':

        ok2 = True
        while ok2:

            print("")
            print("1 - Deposito")
            print("2 - Saque")
            print("3 - Transferencia")
            print("4 - Imprimir lista de transaçoes")
            print("5 - Voltar")

            opmenu = input("\nDigite o numero da opçao desejada: ")

            if opmenu == '5':
                ok2 = False


            if opmenu == '1':

                consultar = input ("\nInforme o codigo da conta em que deseja realizar o deposito: ")
                consultarV = consultar in Contas['cod']

                if consultarV == True:

                    pos = Contas['cod'].index(consultar)
                    deposito = input ("\nInforme o valor do deposito: ")
                    deposito = float(deposito)
                    valor = Contas['saldo'][pos]
                    valor = valor + deposito
                    Contas['saldo'][pos] = valor

                else:
                    input ("Conta nao existe!!")


                ### Lista de trans


            if opmenu == '2':

                consultar = input ("\nInforme o codigo da conta em que deseja realizar o saque: ")
                consultarV = consultar in Contas['cod']

                if consultarV == True:

                    pos = Contas['cod'].index(consultar)
                    saque = input ("\nInforme o valor do saque: ")
                    saque = float(saque)
                    valor = Contas['saldo'][pos]

                    if valor > saque:
                        valor = valor - saque
                        Contas['saldo'][pos] = valor

                    else:
                        input("Saldo insuficiente!!")

                else:
                    input ("Conta nao existe!!")


print ("Finalizando...")
