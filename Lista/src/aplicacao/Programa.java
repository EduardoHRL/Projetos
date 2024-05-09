package aplicacao;

import entidades.Funcionarios;
import java.util.Locale;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.printf("CADASTRO DE FUNCIONÁRIOS");

        System.out.printf("\n\nInforme quantos funcionários deseja cadastrar: ");
        int func = sc.nextInt();

        List<Funcionarios> lista = new ArrayList<>(func);

        for (int i = 1; i <= func; i++) {
            System.out.printf("\nFuncionário #%d:\n", i);

            System.out.printf("ID: ");
            int id = sc.nextInt();

            while (existeId(lista, id)) {
                System.out.print("Id digitado Existente. Digite novamente: ");
                id = sc.nextInt();
            }
            sc.nextLine();

            System.out.printf("Nome: ");
            String nome = sc.nextLine();

            System.out.printf("Salário: ");
            Double salario = sc.nextDouble();

            lista.add(new Funcionarios(id, nome, salario));
        }

        System.out.print("Entre com o Id do funcionário para aumentar o Salário: ");
		int id = sc.nextInt();
		Funcionarios emp = lista.stream().filter(x -> x.getId() == id).findFirst().orElse(null);
		if (emp == null) {
			System.out.println("Este Id não Existe!");
		}
		else {
			System.out.print("Entre com a porcentagem: ");
			double porcentagem = sc.nextDouble();
			emp.AlteraSalario(porcentagem);
		}
            
        

        System.out.printf("\nLista de Funcionários\n");

        for (Funcionarios obj : lista) {
            System.out.println(obj);
        }
        sc.close();

    }

    public static boolean existeId(List<Funcionarios> lista, int id) {
        Funcionarios emp = lista.stream().filter(x -> x.getId() == id).findFirst().orElse(null);
        return emp != null;
    }
}