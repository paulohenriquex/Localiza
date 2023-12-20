def gerenciarVeiculos(connection, cursor):
    while True:
        print("1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Editar veículo")
        print("4 - Excluir veículo")
        print("5 - Voltar")
        opcao = int(input())

        if opcao == 1:
            cadastrarVeiculo(connection, cursor)
        elif opcao == 2:
            listarVeiculos(connection, cursor)
        elif opcao == 3:
            editarVeiculo(connection, cursor)
        elif opcao == 4:
            excluirVeiculo(connection, cursor)
        elif opcao == 5:
            break
        else:
            print("Opção inválida")
            continue


def cadastrarVeiculo(connection, cursor):

    print("1 - Carro")
    print("2 - Caminhao")
    op = int(input())
    if op == 1:
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        ano_modelo = input("Digite o ano do modelo do carro: ")
        ano_fabricacao = input("Digite o ano de fabricação do carro: ")
        placa = input("Digite a placa do carro: ")
        quantidade_portas = int(
            input("Digite a quantidade de portas do carro: "))
        quantidade_passageiros = int(
            input("Digite a quantidade de passageiros do carro: "))

        cursor.execute("INSERT INTO carro(marca,modelo,ano_modelo,ano_fabricacao,placa,quantidade_portas,quantidade_passageiros)VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (marca, modelo, ano_modelo, ano_fabricacao, placa, quantidade_portas, quantidade_passageiros))
        print("Carro cadastrado com sucesso!")
    elif op == 2:
        marca = input("Digite a marca do caminhao: ")
        modelo = input("Digite o modelo do caminhao: ")
        ano_modelo = int(input("Digite o ano do modelo do caminhao: "))
        ano_fabricacao = int(input("Digite o ano de fabricação do caminhao: "))
        placa = input("Digite a placa do caminhao: ")
        quantidade_eixos = int(
            input("Digite a quantidade de eixos do caminhao: "))
        capacidade_carga = float(
            input("Digite a capacidade de carga do caminhao: "))

        cursor.execute("INSERT INTO caminhao(marca,modelo,ano_modelo,ano_fabricacao,placa,quantidade_eixos,capacidade_carga)VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (marca, modelo, ano_modelo, ano_fabricacao, placa, quantidade_eixos, capacidade_carga))
        print("Caminhao cadastrado com sucesso!")

    connection.commit()


def listarVeiculos(connection, cursor):

    print("1 - Carro")
    print("2 - Caminhao")
    op = int(input())

    if op == 1:
        cursor.execute("SELECT * FROM carro")
        carros = cursor.fetchall()
        for carro in carros:
            print(carro)

    elif op == 2:
        cursor.execute("SELECT * FROM caminhao")
        caminhoes = cursor.fetchall()
        for caminhao in caminhoes:
            print(caminhao)


def editarVeiculo(connection, cursor):
    print("1 - Carro")
    print("2 - Caminhao")
    op = int(input())

    if op == 1:
        print("Digite a placa do carro: ")
        placa = input()

        cursor.execute("SELECT * FROM carro WHERE placa = %s", (placa,))
        carro = cursor.fetchone()
        if carro is None:
            print("Carro não encontrado")
            return
        elif carro is not None:
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            ano_modelo = input("Digite o ano do modelo do carro: ")
            ano_fabricacao = input("Digite o ano de fabricação do carro: ")
            placa = input("Digite a placa do carro: ")
            quantidade_portas = int(
                input("Digite a quantidade de portas do carro: "))
            quantidade_passageiros = int(
                input("Digite a quantidade de passageiros do carro: "))
            cursor.execute("UPDATE carro SET marca = %s, modelo = %s, ano_modelo = %s, ano_fabricacao = %s, placa = %s, quantidade_portas = %s, quantidade_passageiros = %s WHERE placa = %s",
                           (marca, modelo, ano_modelo, ano_fabricacao, placa, quantidade_portas, quantidade_passageiros, placa))
            print("Carro atualizado com sucesso!")

    elif op == 2:
        print("Digite a placa do caminhao: ")
        placa = input()

        cursor.execute("SELECT * FROM caminhao WHERE placa = %s", (placa,))
        caminhao = cursor.fetchone()
        if caminhao is None:
            print("Caminhao não encontrado")
            return
        elif caminhao is not None:
            marca = input("Digite a marca do caminhao: ")
            modelo = input("Digite o modelo do caminhao: ")
            ano_modelo = input("Digite o ano do modelo do caminhao: ")
            ano_fabricacao = input("Digite o ano de fabricação do caminhao: ")
            placa = input("Digite a placa do caminhao: ")
            quantidade_eixos = int(
                input("Digite a quantidade de eixos do caminhao: "))
            capacidade_carga = float(
                input("Digite a capacidade de carga do caminhao: "))
            cursor.execute("UPDATE caminhao SET marca = %s, modelo = %s, ano_modelo = %s, ano_fabricacao = %s, placa = %s, quantidade_eixos = %s, capacidade_carga = %s WHERE placa = %s",
                           (marca, modelo, ano_modelo, ano_fabricacao, placa, quantidade_eixos, capacidade_carga, placa))
            print("Caminhao atualizado com sucesso!")


def excluirVeiculo(connection, cursor):
    print("1 - Carro")
    print("2 - Caminhao")
    op = int(input())

    if op == 1:
        cursor.execute("SELECT * FROM carro")
        carros = cursor.fetchall()
        for carro in carros:
            print(carro)
        print("Digite a placa do carro: ")
        placa = input()
        cursor.execute("SELECT * FROM carro WHERE placa = %s", (placa,))
        carro = cursor.fetchone()
        if carro is None:
            print("Carro não encontrado")
            return
        elif carro is not None:
            cursor.execute("DELETE FROM carro WHERE placa = %s", (placa,))
            print("Carro excluido com sucesso!")
    elif op == 2:
        cursor.execute("SELECT * FROM caminhao")
        caminhoes = cursor.fetchall()
        for caminhao in caminhoes:
            print(caminhao)
        print("Digite a placa do caminhao: ")
        placa = input()
        cursor.execute("SELECT * FROM caminhao WHERE placa = %s", (placa,))
        caminhao = cursor.fetchone()
        if caminhao is None:
            print("Caminhao não encontrado")
            return
        elif caminhao is not None:
            cursor.execute("DELETE FROM caminhao WHERE placa = %s", (placa,))
            print("Caminhao excluido com sucesso!")
