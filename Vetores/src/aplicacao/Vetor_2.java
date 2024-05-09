package aplicacao;

import java.util.Locale;
import java.util.Scanner;
import entidades.Produto;

public class Vetor_2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double media = 0;
        double soma = 0;

        System.out.println("Informe a quantidade de produtos a serem lidos: ");
        int p = sc.nextInt();
        Produto[] vetor = new Produto[p];

        for(int i=0,a = 1; i < vetor.length; i++, a++) {
            sc.nextLine();
            System.out.printf("\nInforme o nome do produto %d: ",a);
            String nome = sc.nextLine();
            
            System.out.printf("Informe o preço do produto %d: ",a);
            double preco = sc.nextDouble();
            
            vetor[i] = new Produto(nome,preco);
        }

        for(int i=0; i < vetor.length; i++) {
            soma += vetor[i].getPreco();
        }

        media = soma / p;

        System.out.printf("\nMedia dos preços é: %.2f",media);

        sc.close();
    }
}