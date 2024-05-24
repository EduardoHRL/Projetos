package aplicacao;

import java.util.Scanner;
import java.util.Locale;
import java.util.List;
import java.util.ArrayList;
import entidades.*;

public class App {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Contribuinte> lista = new ArrayList<>();

        System.out.printf("Informe a quantidade de contribuintes: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            sc.nextLine();

            System.out.printf("\nContribuinte #%d: \n", i);
            System.out.printf("Pessoa física ou jurídica? (f/j): ");
            char ch = sc.next().charAt(0);

            sc.nextLine();

            if (ch == 'f') {
                System.out.printf("Nome: ");
                String nome = sc.nextLine();
                System.out.printf("Renda anual: ");
                double renda = sc.nextDouble();
                System.out.printf("Gastos com saúde: ");
                double gastos = sc.nextDouble();
                lista.add(new Fisica(nome, renda, gastos));

            } else if (ch == 'j') {
                System.out.printf("Nome: ");
                String nome = sc.nextLine();
                System.out.printf("Renda anual: ");
                double renda = sc.nextDouble();
                System.out.printf("Quantidade de Funcionarios: ");
                int func = sc.nextInt();
                lista.add(new Juridico(nome, renda, func));
            }
        }
        double total = 0;

        System.out.println("\nTAXAS PAGAS");
        for (Contribuinte x : lista) {
            System.out.printf("\n%s: R$ %.2f", x.getNome(), x.Taxa());
            total = total + x.Taxa();
        }

        System.out.printf("\n\nO total de taxas pagas foi R$ 3%.2f", total);
        sc.close();

    }
}
