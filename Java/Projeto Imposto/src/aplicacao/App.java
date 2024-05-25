//Pacotes\\

package aplicacao; 

//Declaração de Bibliotecas\\
import java.util.Scanner;
import java.util.Locale;
import java.util.List;
import java.util.ArrayList;
import entidades.*;

public class App {
    public static void main(String[] args) {
        
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        //Criação da lista\\
        List<Contribuinte> lista = new ArrayList<>();

        System.out.printf("Informe a quantidade de contribuintes: ");
        int n = sc.nextInt();
        
        //Loop para preencher o nome, renda, gastos com saude ou quantidade de funcionarios\\
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
                //Adiciona os atributos a lista com o construtor de Fisica\\
                lista.add(new Fisica(nome, renda, gastos));

            } else if (ch == 'j') {
                System.out.printf("Nome: ");
                String nome = sc.nextLine();
                System.out.printf("Renda anual: ");
                double renda = sc.nextDouble();
                System.out.printf("Quantidade de Funcionarios: ");
                int func = sc.nextInt();
                //Adiciona os atributos a lista com o construtor de Juridico\\
                lista.add(new Juridico(nome, renda, func));
            }
        }
        double total = 0;

        //Impressão das taxas pagas e o Total\\
        System.out.println("\nTAXAS PAGAS");
        for (Contribuinte x : lista) {
            System.out.printf("\n%s: R$ %.2f", x.getNome(), x.Taxa());
            total = total + x.Taxa();
        }

        System.out.printf("\n\nO total de taxas pagas foi R$ 3%.2f", total);
        sc.close();

    }
}
