package aplicacao;

import entidades.Funcionario;

import java.util.Locale;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        List<Funcionario> lista = new ArrayList<>();

        System.out.printf("CADASTRO DE FUNCIONÁRIOS!!!\n");

        System.out.printf("Informe a quantidade de funcionários: ");
        int funcionarios = sc.nextInt();

        for(int i = 0; i < funcionarios; i++) {
            sc.nextLine();

            System.out.printf("\nNome: ");
            String nome = sc.nextLine();
            
            while(ExisteNome(lista, nome)) {
                System.out.printf("O nome digitado já existe. Digite novamente... ");
                nome = sc.nextLine();
            }

            System.out.printf("Salário: ");
            double salario = sc.nextDouble();

            lista.add(new Funcionario(nome, salario));
        }
        sc.nextLine();
        System.out.printf("\n\nAUMENTO DE SALÁRIO!!!\n");

        System.out.printf("Digite o nome do funcionário: ");
        String nome = sc.nextLine();
        while (lista.stream().anyMatch(x -> x.getNome().equals(nome)) == false) {
            System.out.printf("O nome não existe nos dados. Digite novamente... ");
            nome = sc.nextLine();
        }

        System.out.printf("O aumento será em quantos porcentos: ");
        double aumento = sc.nextDouble();

        sc.close();

    }

    public static boolean ExisteNome(List<Funcionario> lista, String nome) {
        return lista.stream().anyMatch(x -> x.getNome().equals(nome));
    }
}
