import clientes as cli
import veiculos as ve
from datetime import datetime
import uuid


def gerenciarLocacao(connection, cursor):
    while True:
        print("1 - Cadastrar locação")
        print("2 - Listar locações")
        print("3 - Editar locação")
        print("4 - Excluir locação")
        print("5 - Voltar")
        opcao = int(input())

        if opcao == 1:
            cadastrarLocacao(connection, cursor)
        elif opcao == 2:
            listarLocacoes(connection, cursor)
        elif opcao == 3:
            editarLocacao(connection, cursor)
        elif opcao == 4:
            excluirLocacao(connection, cursor)
        elif opcao == 5:
            break
        else:
            print("Opção inválida")
            continue


def cadastrarLocacao(connection, cursor):

    cli.listarClientes(connection, cursor)
    print("Digite o CPF/CNPJ do cliente: ")
    buscarCliente = input()

    cursor.execute(
        "SELECT * FROM clientefisico WHERE cpfcnpj = %s", (buscarCliente,))
    cliente = cursor.fetchone()
    if cliente is None:
        cursor.execute(
            "SELECT * FROM clientejuridico WHERE cpfcnpj = %s", (buscarCliente,))
        cliente = cursor.fetchone()
        if cliente is None:
            print("Cliente não encontrado")
            return

    ve.listarVeiculos(connection, cursor)
    print("Digite a placa do veículo: ")
    buscarVeiculo = input()
    cursor.execute(
        "SELECT * FROM carro WHERE placa = %s", (buscarVeiculo,))
    veiculo = cursor.fetchone()
    if veiculo is None:
        cursor.execute(
            "SELECT * FROM caminhao WHERE placa = %s", (buscarVeiculo,))
        veiculo = cursor.fetchone()
        if veiculo is None:
            print("Veículo não encontrado")
            return

    while True:
        try:
            print("Nome: ", cliente[0])
            print("Endereço: ", cliente[2])

            data_locacao_str = input(
                "Digite a data de locação (formato: DD/MM/AAAA): ")
            data_devolucao_str = input(
                "Digite a data de devolução (formato: DD/MM/AAAA): ")

            data_locacao = datetime.strptime(data_locacao_str, '%d/%m/%Y')
            data_devolucao = datetime.strptime(data_devolucao_str, '%d/%m/%Y')

            valor_diaria = float(input("Digite o valor da diária: "))
            id_locacao = str(uuid.uuid4())

            # Corrigindo a instrução SQL
            cursor.execute("INSERT INTO locacao (data_locacao, data_devolucao, valor_diaria, cpfcnpj_cliente, placa_veiculo, id_locacao) VALUES (%s, %s, %s, %s, %s, %s);",
                           (data_locacao, data_devolucao, valor_diaria, buscarCliente, buscarVeiculo, id_locacao))

            print("Locação cadastrada com sucesso!")

            print("Marca: ", veiculo[1])
            print("Modelo: ", veiculo[2])

            connection.commit()
            break  # Adicionei um break para sair do loop ao obter todas as entradas corretas

        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue


def listarLocacoes(connection, cursor):
    cursor.execute("SELECT * FROM locacao")
    locacoes = cursor.fetchall()

    for locacao in locacoes:
        print("Data Locacao: ", locacao[5])
        print("CPF: ", locacao[0])
        print("Data de Devolucao", locacao[2])
        print("Valor Locacao: ", locacao[3])
        print("ID: ", locacao[4])
        print("")


def editarLocacao(connection, cursor):
    cursor.execute("SELECT * FROM locacao")
    locacoes = cursor.fetchall()

    for locacao in locacoes:
        print("ID", locacao[5])
        print("CPF", locacao[0])
        print("Data de locacao", locacao[2])
        print("Data devolucao", locacao[3])
        print("Valor", locacao[4])
        print("")

    print("Digite o ID da locação: ")
    buscarLocacao = input()
    cursor.execute(
        "SELECT * FROM locacao WHERE id = %s", (buscarLocacao,))
    locacao = cursor.fetchone()
    if locacao is None:
        print("Locação não encontrada")
        return
    elif locacao is not None:
        while True:
            try:
                print("ID: ", locacao[5])
                print("CPF: ", locacao[0])
                print("Data de locacao: ", locacao[2])
                print("Data devolucao: ", locacao[3])
                print("Valor: ", locacao[4])

                data_locacao_str = input(
                    "Digite a data de locação (formato: DD/MM/AAAA): ")
                data_devolucao_str = input(
                    "Digite a data de devolução (formato: DD/MM/AAAA): ")

                data_locacao = datetime.strptime(
                    data_locacao_str, '%d/%m/%Y')
                data_devolucao = datetime.strptime(
                    data_devolucao_str, '%d/%m/%Y')

                valor_diaria = float(input("Digite o valor da diária: "))
                id_locacao = str(uuid.uuid4())

                cursor.execute("UPDATE locacao SET data_locacao = %s, data_devolucao = %s, valor_diaria = %s, id_locacao = %s WHERE id = %s;",
                               (data_locacao, data_devolucao, valor_diaria, id_locacao, buscarLocacao))

                connection.commit()
                print("Locação alterada com sucesso!")
                break

            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue


def excluirLocacao(connection, cursor):
    cursor.execute("SELECT * FROM locacao")
    locacoes = cursor.fetchall()

    for locacao in locacoes:
        print("ID", locacao[5])
        print("CPF", locacao[0])
        print("Data de locacao", locacao[2])
        print("Data devolucao", locacao[3])
        print("Valor", locacao[4])
        print("")

    print("Digite o ID da locação: ")
    buscarLocacao = input()
    cursor.execute(
        "SELECT * FROM locacao WHERE id = %s", (buscarLocacao,))
    locacao = cursor.fetchone()
    if locacao is None:
        print("Locação não encontrada")
        return
    elif locacao is not None:
        cursor.execute("DELETE FROM locacao WHERE id = %s",
                       (buscarLocacao,))
        connection.commit()
        print("Locação excluída com sucesso!")
