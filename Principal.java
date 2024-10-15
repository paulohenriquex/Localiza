import java.util.ArrayList;
import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        int opcao;
        Scanner sc = new Scanner(System.in);
        ArrayList<Clientes> clientes = new ArrayList<>();
        ArrayList<Veiculos> veiculos = new ArrayList<>();
        GerenciarClientes gerCli = new GerenciarClientes();
        GerenciarVeiculos gerVei = new GerenciarVeiculos();

        do {
            System.out.println("1 - Gerenciar clientes.");
            System.out.println("2 - Gerenciar veiculos.");
            System.out.println("0 - Sair.");
            opcao = sc.nextInt();
            sc.nextLine();
            switch (opcao) {
                case 1:
                    gerCli.gerenciarClientes(sc, clientes);
                    break;
                case 2:
                    gerVei.gerenciarVeiculos(sc, veiculos);
                    break;
                default:
                    break;
            }
        } while (opcao != 0);
    }
}
