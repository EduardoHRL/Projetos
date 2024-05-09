package aplicacao;
import java.util.Locale;
import java.util.Scanner;
import entidades.Cliente;

public class TestarCliente {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);
        Cliente cliente1;
        Cliente cliente2;
        Cliente cliente3;

        System.out.println("Cliente 1...");
        System.out.println("\nDigite seu nome: ");
        String nome1 = sc.nextLine();

        System.out.println("Digite seu endereço: ");
        String endereco1 = sc.nextLine();

        System.out.println("Digite sua renda: ");
        Double renda1 = sc.nextDouble();
        sc.nextLine();

        System.out.println("\nCliente 2...");
        System.out.println("\nDigite seu nome: ");
        String nome2 = sc.nextLine();

        System.out.println("Digite seu endereço: ");
        String endereco2 = sc.nextLine();

        System.out.println("Digite sua renda: ");
        Double renda2 = sc.nextDouble();
        sc.nextLine();


        System.out.println("\nCliente 3...");
        System.out.println("\nDigite seu nome: ");
        String nome3 = sc.nextLine();

        System.out.println("Digite seu endereço: ");
        String endereco3 = sc.nextLine();

        System.out.println("Digite sua renda: ");
        Double renda3 = sc.nextDouble();
        sc.nextLine();


        System.out.println("\nDados do cliente1: ");
        cliente1 = new Cliente(nome1, endereco1, renda1);
        cliente1.EscreveDados(nome1, endereco1, renda1);

        System.out.println("\n\nDados do cliente2: ");
        cliente2 = new Cliente(nome2, endereco2, renda2);
        cliente2.EscreveDados(nome2, endereco2, renda2);

        System.out.println("\n\nDados do cliente3: ");
        cliente3 = new Cliente(nome3, endereco3, renda3);
        cliente3.EscreveDados(nome3, endereco3, renda3);



        sc.close();

    }
}
