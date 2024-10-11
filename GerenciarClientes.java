import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;
import java.util.Scanner;
import java.time.format.DateTimeFormatter;

public class GerenciarClientes {
    public void gerenciarClientes(Scanner sc, ArrayList<Clientes> clientes) {

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
            } else if (opcao == 3) {
                alterarCliente(sc, clientes);
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
        } else if (cpfcnpj.length() == 15) {

            System.out.println("Digite o nome do cliente: ");
            String nome = sc.nextLine();

            System.out.println("Digite o nome da cidade: ");
            String cidade = sc.nextLine();

            System.out.println("Digite o nome da rua: ");
            String rua = sc.nextLine();

            System.out.println("Digite o número da casa: ");
            int numero = sc.nextInt();
            sc.nextLine();

            PessoaJuridica pessoaJuridica = new PessoaJuridica(cpfcnpj, nome, rua, cidade, numero);
            clientes.add(pessoaJuridica);

        } else {
            System.out.println("O numero digitado está incorreto, por favor digite novamente.");
            return;
        }
    }

    public static void mostrarClientes(Scanner sc, ArrayList<Clientes> clientes) {
        int opcao;
        System.out.println("1 - Pessoa Física");
        System.out.println("2 - Pessoa Jurídica");
        System.out.println("3 - Fisica/Jurídica");
        opcao = sc.nextInt();
        sc.nextLine();

        if (opcao == 1) {

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

            System.out.println("\n#########################################################");
        } else if (opcao == 2) {

            System.out.println("\n");
            System.out.println("################### Clientes cadastrados ###################");

            for (Clientes cli : clientes) {

                if (cli instanceof PessoaJuridica) {
                    PessoaJuridica pessoaJuridica = (PessoaJuridica) cli;
                    System.out.println("");
                    System.out.println("Nome: " + pessoaJuridica.getNome());
                    System.out.println("CNPJ: " + pessoaJuridica.getCnpj());
                    System.out.println("Rua: " + pessoaJuridica.getRua());
                    System.out.println("Cidade: " + pessoaJuridica.getCidade());
                    System.out.println("Numero: " + pessoaJuridica.getNumero());
                }
            }

            System.out.println("\n#########################################################");

        } else if (opcao == 3) {

            System.out.println("\n");
            System.out.println("################### Clientes cadastrados ###################");

            for (Clientes cli : clientes) {
                PessoaJuridica pessoaJuridica = (PessoaJuridica) cli;
                System.out.println("");
                System.out.println("Nome: " + pessoaJuridica.getNome());
                System.out.println("CNPJ: " + pessoaJuridica.getCnpj());
                System.out.println("Rua: " + pessoaJuridica.getRua());
                System.out.println("Cidade: " + pessoaJuridica.getCidade());
                System.out.println("Numero: " + pessoaJuridica.getNumero());

            }

            System.out.println("\n#########################################################");

        } else {
            System.out.println("Opção inválida");
        }
    }

    public static void alterarCliente(Scanner sc, ArrayList<Clientes> clientes) {

        System.out.println("Digite o CPF/CNPJ do cliente que deseja alterar: ");
        String buscarCpfCnpj = sc.nextLine();

        if (buscarCpfCnpj.length() == 11) {

            for (Clientes cli : clientes) {
                if (cli instanceof PessoaFisica) {
                    PessoaFisica pessoaFisica = (PessoaFisica) cli;
                    if (pessoaFisica.getCpf().equals(buscarCpfCnpj)) {

                        System.out.println("Cliente encontrado com sucesso " + pessoaFisica.getNome());

                        System.out.println("Digite o novo nome: ");
                        String novoNome = sc.nextLine();

                        System.out.println("Digite o novo CPF: ");
                        String novoCPF = sc.nextLine();

                        System.out.println("Digite o novo nome da cidade: ");
                        String novoNomeCidade = sc.nextLine();

                        System.out.println("Digite o novo nome da rua: ");
                        String rua = sc.nextLine();

                        System.out.println("Digite o novo numero: ");
                        int novoNumero = sc.nextInt();
                        sc.nextLine();

                        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy");
                        System.out.println("Digite a nova data de nascimento: ");
                        String dataNas = sc.nextLine();

                        try {
                            System.out.println("Entrou no try");
                            LocalDate dataDeNascimento = LocalDate.parse(dataNas, formatter);
                            System.out.println("1");
                            LocalDate dataAtual = LocalDate.now();
                            System.out.println("2");
                            int verificarIdade = Period.between(dataDeNascimento, dataAtual).getYears();
                            System.out.println("3");
                            System.out.println("Sua idade é: " + verificarIdade);
                            if (verificarIdade >= 18 && verificarIdade <= 115) {
                                pessoaFisica.setNome(novoNome);
                                pessoaFisica.setCpf(novoCPF);
                                pessoaFisica.setCidade(novoNomeCidade);
                                pessoaFisica.setRua(rua);
                                pessoaFisica.setNumero(novoNumero);
                                pessoaFisica.setDataDeNascimento(dataDeNascimento);
                            }
                        } catch (Exception e) {
                            System.out.println("Falha ao digitar a data. " + e.getMessage());
                        }

                    }

                }
            }
        } else if (buscarCpfCnpj.length() == 15) {

            for (Clientes cli : clientes) {
                if (cli instanceof PessoaJuridica) {
                    PessoaJuridica pessoaJuridica = (PessoaJuridica) cli;
                    if (pessoaJuridica.getCnpj().equals(buscarCpfCnpj)) {

                        System.out.println("Cliente encontrado com sucesso " + pessoaJuridica.getNome());

                        System.out.println("Digite o novo nome: ");
                        String novoNome = sc.nextLine();

                        System.out.println("Digite o novo CNPJ: ");
                        String novoCNPJ = sc.nextLine();

                        System.out.println("Digite o novo nome da cidade: ");
                        String novoNomeCidade = sc.nextLine();

                        System.out.println("Digite o novo nome da rua: ");
                        String rua = sc.nextLine();

                        System.out.println("Digite o novo numero: ");
                        int novoNumero = sc.nextInt();
                        sc.nextLine();

                        pessoaJuridica.setNome(novoNome);
                        pessoaJuridica.setCnpj(novoCNPJ);
                        pessoaJuridica.setCidade(novoNomeCidade);
                        pessoaJuridica.setRua(rua);
                        pessoaJuridica.setNumero(novoNumero);
                    }

                }
            }

        }

    }
}