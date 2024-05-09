package aplicacao;

import java.util.Locale;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import entidades.Pessoa;

public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.printf("Quantas pessoas serão digitadas: ");
        int pessoas = sc.nextInt();

        List<Pessoa> lista = new ArrayList<>();

        for (int i = 1; i <= pessoas; i++) {
            sc.nextLine();

            System.out.printf("\n\nDados da %dª pessoa:\n", i);

            System.out.printf("Nome: ");
            String nome = sc.nextLine();

            while (existeNome(lista, nome)) {
                System.out.println("O nome já existe na lista. Digite novamente: ");
                nome = sc.nextLine();
            }

            System.out.printf("Idade: ");
            int idade = sc.nextInt();

            lista.add(new Pessoa(nome, idade));
        }

        Pessoa PessoaMaisVelha = MaiorIdade(lista);

        System.out.printf("A pessoa mais velha é: %s", PessoaMaisVelha);

        sc.close();
    }

    public static boolean existeNome(List<Pessoa> lista, String nome) {
        return lista.stream().anyMatch(x -> x.getNome().equals(nome));
    }

    public static Pessoa MaiorIdade(List<Pessoa> lista) {
        int MaiorIdade = 0;
        Pessoa PessoaMaisVelha = null;

        for (Pessoa x : lista) {
            if (x.getIdade() > MaiorIdade) {
                MaiorIdade = x.getIdade();
                PessoaMaisVelha = x;
            }
        }
        return PessoaMaisVelha;
    }

}
