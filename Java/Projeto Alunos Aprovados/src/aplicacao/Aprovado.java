package aplicacao;

import java.util.Locale;
import java.util.Scanner;
import entidades.Alunos;

public class Aprovado {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double ap = 0;

        System.out.printf("Informe a quantidade de alunos que deseja: ");
        int aluno = sc.nextInt();
        Alunos[] vetor = new Alunos[aluno];

        for (int i = 0; i < aluno; i++) {
            sc.nextLine();

            System.out.printf("\nAluno %d\n", i);

            System.out.printf("Nome: ");
            String nome = sc.nextLine();

            System.out.printf("Informe a primeira nota (0-100): ");
            double nota1 = sc.nextDouble();

            System.out.printf("Informe a segunda nota (0-100): ");
            double nota2 = sc.nextDouble();

            ap = (nota1 + nota2) / 2;

            if (ap >= 60) {
                vetor[i] = new Alunos(nome);
            }
        }

        System.out.printf("\nAlunos aprovados com média maior que 60: ");

        for (int i = 0; i < aluno; i++) {
            if (vetor[i] != null) {
                System.out.printf("\n%s", vetor[i].getNome());
            }
        }

        sc.close();
    }
}