package aplicacao;

import entidades.*;
import java.util.Scanner;
import java.util.Locale;
import java.util.List;
import java.util.ArrayList;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        List<Produto> lista = new ArrayList<>();

        System.out.printf("Informe a quantidade de produtos: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            sc.nextLine();

            System.out.println("Produto #" + i);
            System.out.println("O produto é comum, usado ou importado? ");
            String condicao = sc.nextLine();
            condicao = condicao.toLowerCase();

            System.out.println("Nome: ");
            String nome = sc.nextLine();
            System.out.println("Preço: ");
            double preco = sc.nextDouble();

            if (condicao == "usado") {
                System.out.println("Informe a data de fabricação do produto: ");
                String data = sc.nextLine();
                LocalDate dataF = LocalDate.parse(data, formatter);
            }
            else if(condicao == "importado") {
                System.out.println("Informe a taxa alfandegária do produto: ");
                double taxa = sc.nextDouble();
            }
        }

        System.out.println("\n\nTAGS DE PREÇO\n");

        for (int i = 0; i < n; i++) {
            
        }

    }
}