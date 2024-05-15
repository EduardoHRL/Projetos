package aplicacao;

import entidades.Funcionarios;

import java.util.Locale;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;


public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        DateTimeFormatter fmt1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        LocalDate data = LocalDate.now();


        List<Funcionarios> lista = new ArrayList<>();

        System.out.printf("Digite a quantidade de Funcionários: ");
        int quantidade = sc.nextInt();

        for (int i = 1; i <= quantidade; i++) {
            sc.nextLine();

            System.out.printf("\nFUNCIONÁRIO #%d\n", i);

            System.out.printf("Nome: ");
            String nome = sc.nextLine();

            while (existeNome(lista, nome)) {
                System.out.printf("O nome já existe. Digite novamente... ");
                nome = sc.nextLine();
            }

            System.out.printf("Salario: ");
            double salario = sc.nextDouble();

            lista.add(new Funcionarios(nome, salario));
        }
        sc.nextLine();

        System.out.printf("\n\nDeseja aumentar o salário de algum funcionário? (s p/ Sim ou n p/ Não): ");
        String escolha = sc.nextLine();

        if (escolha.equals("s")) {
            System.out.printf("\nInforme o nome do funcionário: ");
            String nome = sc.nextLine();

            Funcionarios funcionario = lista.stream().filter(x -> x.getNome().equals(nome)).findFirst().orElse(null);

            while (funcionario == null) {
                System.out.println("O funcionário não existe. Digite novamente...");
                String func = sc.nextLine();
                funcionario = lista.stream().filter(x -> x.getNome().equals(func)).findFirst().orElse(null);
            }

            System.out.printf("Informe a porcentagem de aumento: ");
            double porcentagem = sc.nextDouble();

            double salario = funcionario.getSalario();
            funcionario.aumentarSalario(porcentagem);

            System.out.printf("\n\nO funcionário escolhido foi %s\n", funcionario.getNome());
            System.out.printf("O salario era %.2f reais\n", salario);
            System.out.printf("O aumento foi de %.2f%%\n", porcentagem);
            System.out.printf("O salario agora é de %.2f reais\n", funcionario.getSalario());

            System.out.println("Data: "+ data.format(fmt1));
        }
        else {
            System.out.printf("FINALIZANDO...");
            System.exit(0);
        }
        sc.close();

    }

    public static boolean existeNome(List<Funcionarios> lista, String nome) {
        return lista.stream().anyMatch(x -> x.getNome().equals(nome));
    }

}
