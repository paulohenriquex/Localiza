import psycopg2
import clientes as cl
import veiculos as ve
import locacao as loc
import caixa as cx


def conectar_banco():
    # Parâmetros de conexão ao banco de dados
    db_params = {
        'host': 'localhost',
        'database': 'Locadora',
        'user': 'postgres',
        'password': '121255qq'
    }

    try:
        # Conecte-se ao banco de dados
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        return connection, cursor

    except Exception as e:
        print(f"Erro de conexão: {e}")
        return None, None


def fechar_conexao(connection, cursor):
    # Certifique-se de fechar a conexão quando terminar
    if connection:
        cursor.close()
        connection.close()


def main():
    connection, cursor = conectar_banco()

    if connection is None or cursor is None:
        print("Erro na conexão com o banco de dados.")
        return

    while True:
        print("1 - Clientes")
        print("2 - Veículos")
        print("3 - Locações")
        print("4 - Caixa")
        print("5 - Sair")
        opcao = int(input())

        if opcao == 1:
            cl.gerenciarClientes(connection, cursor)
        elif opcao == 2:
            ve.gerenciarVeiculos(connection, cursor)
        elif opcao == 3:
            loc.gerenciarLocacao(connection, cursor)
        elif opcao == 4:
            cx.gerenciarCaixa(connection, cursor)
        elif opcao == 5:
            fechar_conexao(connection, cursor)
            break
        else:
            print("Opção inválida")
            continue


if __name__ == "__main__":
    main()
