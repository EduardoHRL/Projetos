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

            System.out.printf("\nContribuinte #1: ");
            System.out.printf("Pessoa física ou jurídica? ");
            String pessoa = sc.nextLine().toLowerCase().trim();

            if (pessoa == "fisica") {
                System.out.printf("Nome: ");
                String nome = sc.nextLine();
                System.out.printf("Renda anual: ");
                double renda = sc.nextDouble();
                System.out.printf("Gastos com saúde: ");
                double gastos = sc.nextDouble();
                lista.add(new Contribuinte(nome, renda, gastos));

            } else if (pessoa == "juridica") {
                System.out.printf("Nome: ");
                String nome = sc.nextLine();
                System.out.printf("Renda anual: ");
                double renda = sc.nextDouble();
                System.out.printf("Quantidade de Funcionarios: ");
                int func = sc.nextInt();
                lista.add(new Contribuinte(nome, renda, func));
            }

        }

    }
}
