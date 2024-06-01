package aplicacao;

import java.util.Scanner;
import entidades.*;

public class TestaMidia {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        Midia[] lista = new Midia[10];

        int opcao;

        for (int i = 0; i < 2; i++) {
            System.out.printf("Digite 1 para CD e 2 para DVD");
            opcao = in.nextInt();
            if (1 == opcao) {
                lista[i] = new Cd();
                lista[i].insereDados();
            } else {
                lista[i] = new Dvd();
                lista[i].insereDados();
            }
        }

        for (int i = 0; i < 2; i++) {
            lista[i].printDados();
        }

    }
}