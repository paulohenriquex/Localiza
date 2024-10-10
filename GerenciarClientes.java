import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;

import javax.annotation.processing.Generated;

import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class GerenciarClientes {
    public static void gerenciarClientes(Scanner sc, ArrayList<Clientes> clientes) {

        int opcao;

        do {
            System.out.println("");
            System.out.println("1 - Cadastrar clientes");
            System.out.println("2 - Mostrar clientes");
            System.out.println("3 - Alterar cliente");
            System.out.println("4 - Excluir cliente");
            System.out.println("0 - Sair");
            opcao = sc.nextInt();
            sc.nextLine();
            System.out.println("");
            if (opcao == 1) {
                cadastrarClientes(sc, clientes);
            } else if (opcao == 2) {
                mostrarClientes(sc, clientes);
            }

        } while (opcao != 0);

    }

    public static void cadastrarClientes(Scanner sc, ArrayList<Clientes> clientes) {

        System.out.println("Digite o nome cpf/cnpj do cliente: ");
        String cpfcnpj = sc.nextLine();

        if (cpfcnpj.length() == 11) {

            System.out.println("Digite o nome do cliente: ");
            String nome = sc.nextLine();

            System.out.println("Digite o nome da cidade: ");
            String cidade = sc.nextLine();

            System.out.println("Digite o nome da rua: ");
            String rua = sc.nextLine();

            System.out.println("Digite o número da casa: ");
            int numero = sc.nextInt();

            sc.nextLine();

            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy");
            System.out.println("Digite a data de nascimento: ");
            String dataNas = sc.nextLine();

            try {
                LocalDate dataDeNascimento = LocalDate.parse(dataNas, formatter);
                System.out.println("Data de nascimento: " + dataDeNascimento);
                PessoaFisica pessoaFisica = new PessoaFisica(cpfcnpj, dataDeNascimento, nome, rua, cidade, numero);
                clientes.add(pessoaFisica);
            } catch (Exception e) {
                System.out.println("Formato da data foi digitado errado use o formato dd-MM-yyyy.");
            }
        }else if(cpfcnpj.length()==15){
            //!  TODO FAZER MAIS TARDE
        }else{
            System.out.println("O numero digitado está incorreto, por favor digite novamente.");
            return;
        }
    }

    public static void mostrarClientes(Scanner sc, ArrayList<Clientes> clientes) {
        System.out.println("\n");
        System.out.println("################### Clientes cadastrados ###################");

        for (Clientes cli : clientes) {

            if (cli instanceof PessoaFisica) {
                PessoaFisica pessoaFisica = (PessoaFisica) cli;
                System.out.println("");
                System.out.println("Nome: " + pessoaFisica.getNome());
                System.out.println("CPF: " + pessoaFisica.getCpf());
                System.out.println("Rua: " + pessoaFisica.getRua());
                System.out.println("Cidade: " + pessoaFisica.getCidade());
                System.out.println("Numero: " + pessoaFisica.getNumero());
                System.out.println("Data de nascimento: " + pessoaFisica.getDataDeNascimento());
            }
        }
    }
}