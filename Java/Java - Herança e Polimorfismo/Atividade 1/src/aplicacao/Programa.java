package aplicacao;

import java.util.Locale;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import entidades.*;

public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Midia> lista = new ArrayList<>();

        System.out.printf("Informe a quantidade de Midias: ");
        int n = sc.nextInt();
        sc.nextLine();

        for (int i = 1; i <= n; i++) {
            System.out.printf("Deseja cadastrar um CD ou um DVD? ");
            String opcao = sc.next().trim().toUpperCase();

            if("CD".equals(opcao)) {
                Cd cd = new Cd();
                cd.insereDados();
                lista.add(cd);
            }
            else if("DVD".equals(opcao)){
                Dvd dvd = new Dvd();
                dvd.insereDados();
                lista.add(dvd);
            } else {
                System.out.println("Opção invalida. Digite novamente... ");
                i--;
            }
        }

        for (Midia x : lista) {
            System.out.println(x);
        }
        for(int i = 0; i < n; i++) {
            Midia m = new Cd();
            m.printDados();

        }
        
        sc.close();
    }
}
