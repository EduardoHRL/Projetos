package aplicacao;

import java.util.Locale;
import java.util.Scanner;
import entidades.Data;

public class TestarData {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);
        Data hoje;
        Data natal;

        System.out.println("Digite o dia da data: ");
        int dia = sc.nextInt();

        System.out.println("Digite o mês da data: ");
        int mes = sc.nextInt();

        System.out.println("Digite o ano da data: ");
        int ano = sc.nextInt();

        hoje = new Data(dia, mes, ano);
        hoje.escreverAData();

        System.out.println("\nNATAL!\n");

        System.out.println("Digite o dia do natal: ");
        int dianatal = sc.nextInt();

        System.out.println("Digite o mês do natal: ");
        int mesnatal = sc.nextInt();

        System.out.println("Digite o ano do natal: ");
        int anonatal = sc.nextInt();

        natal = new Data(dianatal, mesnatal, anonatal);
        natal.escreverAData();

        sc.close();
    }
}
