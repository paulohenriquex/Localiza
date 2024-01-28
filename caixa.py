import locacao as lc
import datetime
import uuid


def gerenciarCaixa(connection, cursor):
    while True:
        print("1 - Realizar pagamento locacao ")
        print("2 - Relatorio pagamento em dia ")
        print("3 - Relatorio pagamento atrasado ")
        opcao = int(input())

        if opcao == 1:
            pagamentoLocacao(connection, cursor)
        elif opcao == 2:
            relatorioPagamentoDia(connection, cursor, lc)
        elif opcao == 3:
            editarCaixa(connection, cursor)
        elif opcao == 4:
            excluirCaixa(connection, cursor)
        elif opcao == 5:
            break
        else:
            print("Opção inválida")
            continue


def pagamentoLocacao(connection, cursor):
    valor = 0

    lc.listarLocacoes(connection, cursor)

    buscarLocacao = input("Digite o id da locação: ")
    cursor.execute(
        "SELECT * FROM locacao WHERE id_locacao = %s", (buscarLocacao,))
    locacao = cursor.fetchone()

    print("Data Locacao: ", locacao[5])
    print("Data Devolução: ", locacao[2])
    print("Placa: ", locacao[1])
    print("CPF: ", locacao[0])
    print("Valor: ", locacao[3])
    print("ID: ", locacao[4])

    if locacao is None:
        print("Locação não encontrada.")
        return
    elif locacao is not None:
        while True:
            try:
                data_pagamento_str = input(
                    "Digite a data de pagamento (formato: DD/MM/AAAA): ")
                data_pagamento = datetime.datetime.strptime(
                    data_pagamento_str, '%d/%m/%Y')

                data_locacao = datetime.datetime.strptime(
                    locacao[5].strftime('%d-%m-%Y'), '%d-%m-%Y')

                dias = (data_pagamento - data_locacao).days

                if dias < 0:
                    raise ValueError(
                        "A data de pagamento deve ser posterior à data de locação.")

                valor = locacao[3] * dias
                print("Valor a ser pago: ", valor)
                id_pagamento = str(uuid.uuid4())
                break
            except ValueError as e:
                print(f"Erro: {e}")
                continue

        cursor.execute("INSERT INTO caixa (data_pagamento, id_pagamento, valor, id_locacao) VALUES (%s, %s, %s, %s)",
                       (data_pagamento, id_pagamento, valor, buscarLocacao))

        connection.commit()
        print("Locação paga com sucesso.")


def relatorioPagamentoDia(connection, cursor, lc):
    cursor.execute("SELECT * FROM caixa")
    caixas = cursor.fetchall()

    for caixa in caixas:
        data_pagamento_str = caixa[1]
        data_pagamento = datetime.datetime.strptime(
            data_pagamento_str, '%Y-%m-%d')

        if data_pagamento < datetime.today().date():
            cursor.execute(
                "SELECT * FROM locacao WHERE id_locacao = %s", (caixa[3],))
            locacao = cursor.fetchone()

            print("Data Locacao: ", locacao[5])
            print("Data Devolução: ", locacao[2])
            print("Placa: ", locacao[1])
            print("CPF: ", locacao[0])
            print("Valor: ", locacao[3])
            print("ID: ", locacao[4])
            print("")

    if not caixas:
        print("Nenhum pagamento realizado hoje.")
        print("Teste")
        return
