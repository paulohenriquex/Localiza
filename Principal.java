import java.util.Scanner;
import java.util.ArrayList;

public class Principal {

    
    public static void main(String[]agv){
        ArrayList<Clientes> clientes = new ArrayList<>();

        int opcao;
        Scanner sc = new Scanner(System.in);
        GerenciarClientes gerCli = new GerenciarClientes();
        
        do {

            System.out.println("1 - Gerenciar Clientes");
            System.out.println("2 - Gerenciar Veiculos");
            System.out.println("3 - Gerenciar Locação");
            System.out.println("4 - Gerenciar Pagamentos");
            System.out.println("0 - Sair");
            opcao = sc.nextInt();
            sc.nextLine();
            if(opcao == 1){
                gerCli.gerenciarClientes(sc,clientes);
            }
            
        } while (opcao!=0);
    }
}
