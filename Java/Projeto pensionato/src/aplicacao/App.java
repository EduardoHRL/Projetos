package aplicacao;

import java.util.Locale;
import java.util.Scanner;
import entidades.Alunos;

public class App {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int q = 0;

        System.out.printf("Informe a quantidade de quartos que serão alugados: (1-10) ");
        int quartos = sc.nextInt();
        while (quartos <= 0 || quartos > 10) {
            System.out.println("\nInforme a quantidade de alunos de 1 a 10!");
            System.out.printf("Informe a quantidade de quartos que serão alugados: (1-10) ");
            quartos = sc.nextInt();
        }
        Alunos[] vetor = new Alunos[11];
        int[] vet = new int[10];

        for (int i = 0, a =1; i < quartos; i++, a++) {
            sc.nextLine();

            System.out.printf("\nAluguel %d\n",a);

            System.out.printf("Nome: ");
            String nome = sc.nextLine();

            System.out.printf("Email: ");
            String email = sc.nextLine();

            System.out.printf("Quarto alugado: (0-9) ");
            q = sc.nextInt();
            while (q < 0 || q > 9) {
                System.out.printf("\nInforme o quarto alugado de 0 a 9!");
                System.out.printf("Quarto alugado: (0-9)");
                q = sc.nextInt();
            }
           

            vet[i] = q;
            vetor[q] = new Alunos(nome, email);
            
            
        }

        System.out.printf("\n\nQuartos ocupados...");
        for (int i = 0; i < quartos; i++) {
            System.out.printf("\n%d: %s, %s", vet[i], vetor[vet[i]].getNome(), vetor[vet[i]].getEmail());
        }

        sc.close();
    }
}
