from datetime import datetime


def gerenciarClientes(connection, cursor):
    while True:
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Editar cliente")
        print("4 - Excluir cliente")
        print("5 - Voltar")
        opcao = int(input())

        if opcao == 1:
            cadastrarcliente(connection, cursor)
        elif opcao == 2:
            listarClientes(connection, cursor)
        elif opcao == 3:
            alterarCliente(connection, cursor)
        elif opcao == 4:
            excluirCliente(connection, cursor)
        elif opcao == 5:
            break
        else:
            print("Opção inválida")
            continue


def cadastrarcliente(connection, cursor):
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    cpfcnpj = input("Digite o CPF/CNPJ do cliente: ")
    status = 0

    if len(cpfcnpj) == 11:
        while True:
            try:
                data_nascimento_str = input(
                    "Digite a data de nascimento (formato: DD/MM/AAAA): ")
                data_nascimento = datetime.strptime(
                    data_nascimento_str, '%d/%m/%Y')

                # Verifica se a data de nascimento é válida
                if data_nascimento.year < 1900 or data_nascimento > datetime.now():
                    raise ValueError("Data inválida")

                break  # Adicionei este break para sair do loop ao obter uma data válida

            except ValueError:
                print("Data inválida. Tente novamente.")
                continue

        cursor.execute("INSERT INTO clientefisico (nome, endereco, telefone, cpfcnpj, data_nascimento) VALUES (%s, %s, %s, %s, %s);",
                       (nome, endereco, telefone, cpfcnpj, data_nascimento))
        connection.commit()
        print("Cliente cadastrado com sucesso!")

    elif len(cpfcnpj) == 14:
        cnpj = cpfcnpj
        # Adicionei esta linha para obter o CNPJ
        cnpj = input("Digite o CNPJ: ")
        cursor.execute("INSERT INTO clientejuridico (nome, endereco, telefone, cpfcnpj) VALUES (%s, %s, %s, %s);",
                       (nome, endereco, telefone, cpfcnpj))
        connection.commit()
        print("Cliente cadastrado com sucesso!")

    else:
        print("CPF/CNPJ inválido")


def listarClientes(connection, cursor):
    print("1 - Listar clientes físicos")
    print("2 - Listar clientes jurídicos")
    opcao = int(input())

    if opcao == 1:
        print("Listar clientes Pessoa Física")
        cursor.execute("SELECT * FROM clientefisico")
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(cliente)
    elif opcao == 2:
        print("Listar clientes Pessoa Jurídica")
        cursor.execute("SELECT * FROM clientejuridico")
        clientejuridicos = cursor.fetchall()
        for clientejuridico in clientejuridicos:
            print(clientejuridico)


def alterarCliente(connection, cursor):
    print("1 - Cliente pessoa fisica")
    print("2 - Cliente pessoa juridica")
    opcao = int(input())

    if opcao == 1:
        print("Digite o CPF do cliente: ")
        buscarCliente = input()
        cursor.execute(
            "SELECT * FROM clientefisico WHERE cpfcnpj = %s", (buscarCliente,))
        cliente = cursor.fetchone()
        if cliente is None:
            print("Cliente não encontrado")
            return

        while True:
            try:
                print("Nome: ", cliente[0])
                print("Endereço: ", cliente[2])
                print("Telefone: ", cliente[3])
                print("Data de nascimento: ", cliente[4])

                nome = input("Digite o nome do cliente: ")
                endereco = input("Digite o endereço do cliente: ")
                telefone = input("Digite o telefone do cliente: ")

                data_nascimento_str = input(
                    "Digite a data de nascimento (formato: DD/MM/AAAA): ")
                data_nascimento = datetime.strptime(
                    data_nascimento_str, '%d/%m/%Y')

                # Verifica se a data de nascimento é válida
                if data_nascimento.year < 1900 or data_nascimento > datetime.now():
                    raise ValueError("Data inválida")

                cursor.execute("UPDATE clientefisico SET nome = %s, endereco = %s, telefone = %s, data_nascimento = %s WHERE cpfcnpj = %s;",
                               (nome, endereco, telefone, data_nascimento, buscarCliente))
                connection.commit()
                print("Cliente alterado com sucesso!")
                break  # Adicionei um break para sair do loop ao obter todas as entradas corretas

            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

    elif opcao == 2:
        print("Digite o CNPJ do cliente: ")
        buscarCliente = input()
        cursor.execute(
            "SELECT * FROM clientejuridico WHERE cpfcnpj = %s", (buscarCliente,))
        cliente = cursor.fetchone()
        if cliente is None:
            print("Cliente não encontrado")
            return

        while True:
            try:
                print("Nome: ", cliente[0])
                print("Endereço: ", cliente[2])
                print("Telefone: ", cliente[3])

                nome = input("Digite o nome do cliente: ")
                endereco = input("Digite o endereço do cliente: ")
                telefone = input("Digite o telefone do cliente: ")

                cursor.execute("UPDATE clientejuridico SET nome = %s, endereco = %s, telefone = %s WHERE cpfcnpj = %s;",
                               (nome, endereco, telefone, buscarCliente))
                connection.commit()
                print("Cliente alterado com sucesso!")
                break  # Adicionei um break para sair do loop ao obter todas as entradas corretas

            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue


def excluirCliente(connection, cursor):
    print("1 - Cliente pessoa fisica")
    print("2 - Cliente pessoa juridica")
    opcao = int(input())

    if opcao == 1:
        print("Digite o CPF do cliente: ")
        buscarCliente = input()
        cursor.execute(
            "SELECT * FROM clientefisico WHERE cpfcnpj = %s", (buscarCliente,))
        cliente = cursor.fetchone()
        if cliente is None:
            print("Cliente não encontrado")
            return
        elif cliente is not None:
            cursor.execute(
                "DELETE FROM clientefisico WHERE cpfcnpj = %s;", (buscarCliente,))
            connection.commit()
            print("Cliente excluido com sucesso!")
            return

    elif opcao == 2:
        print("Digite o CNPJ do cliente: ")
        buscarCliente = input()
        cursor.execute(
            "SELECT * FROM clientejuridico WHERE cpfcnpj = %s", (buscarCliente,))
        cliente = cursor.fetchone()
        if cliente is None:
            print("Cliente não encontrado")
            return
        elif cliente is not None:
            cursor.execute(
                "DELETE FROM clientejuridico WHERE cpfcnpj = %s;", (buscarCliente,))
            connection.commit()
            print("Cliente excluido com sucesso!")
            return
