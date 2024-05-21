package aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class ForEach {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        String[] vetor = new String[] { "Maria", "Bob", "Alex" };

        for (int i = 0; i < vetor.length; i++) {
            System.out.printf(vetor[i]);
        }
        for (String objeto : vetor) {
            System.out.printf(objeto);
        }

        sc.close();

    }
}
