import java.util.ArrayList;
import java.util.Scanner;

public class GerenciarVeiculos {

    public void gerenciarVeiculos(Scanner sc, ArrayList<Veiculos> veiculos) {
        int opcao;

        do {
            System.out.println("1 - Cadastrar veiculos");
            System.out.println("2 - Mostrar veículos");
            System.out.println("3 - Alterar veículo");
            System.out.println("4 - Excluir veículo");
            System.out.println("0 - Sair");
            opcao = sc.nextInt();
            sc.nextLine();
            switch (opcao) {
                case 1:
                    cadastrarVeiculo(sc, veiculos);
                    break;
                case 2:
                    mostrarVeiculos(sc, veiculos);
                    break;
                case 3:
                    System.out.println("Alterar veículo");
                    break;
                case 4:
                    System.out.println("Excluir veículo");
                    break;
                case 0:
                    System.out.println("Saindo do sistema de veículos.");
                    break;
                default:
                    System.out.println("Opção inválida.");
                    break;
            }
        } while (opcao != 0);
    }

    public static void cadastrarVeiculo(Scanner sc, ArrayList<Veiculos> veiculos) {

        int op;

        do {

            System.out.println("1 - Cadastrar carro.");
            System.out.println("2 - Cadastrar caminhão.");
            System.out.println("0 - Sair");
            op = sc.nextInt();

            if (op == 0) {
                break;
            }

            sc.nextLine();
            if (op == 1) {

                System.out.println("Digite a placa do carro: ");
                String placa = sc.nextLine();

                System.out.println("Digite a marca do carro: ");
                String marca = sc.nextLine();

                System.out.println("Digite o modelo do carro: ");
                String modelo = sc.nextLine();

                System.out.println("Digite a cor do carro: ");
                String cor = sc.nextLine();

                System.out.println("Digite o ano de fabricação: ");
                int anoDeFabricacao = sc.nextInt();
                sc.nextLine();

                System.out.println("Digite a quantidade de portas: ");
                int quantiaddeDePortas = sc.nextInt();
                sc.nextLine();

                Veiculos veiculo = new Carros(placa, marca, modelo, cor, anoDeFabricacao, quantiaddeDePortas);
                veiculos.add(veiculo);
            }
        } while (op != 0);
    }

    public static void mostrarVeiculos(Scanner sc, ArrayList<Veiculos> veiculos) {
        for (Veiculos vei : veiculos) {
            if (vei instanceof Carros) {
                Carros carros = (Carros) vei;
                System.out.println("Placa: " + carros.getPlaca());
                System.out.println("Marca: " + carros.getMarca());
                System.out.println("Modelo: " + carros.getModelo());
                System.out.println("Cor: " + carros.getCor());
                System.out.println("Ano: " + carros.getAnoFabricacao());
                System.out.println("Quantidade Portas: " + carros.getQuantidadeDePortas());
            }
        }
    }
}