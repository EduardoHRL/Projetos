package aplicacao;

import java.util.Scanner;
import entidades.*;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Veiculos veiculo = null;
        
        System.out.println("Deseja cadastrar uma moto ou um carro? ");
        String opcao = sc.nextLine().toLowerCase();

        System.out.println();
        if (opcao.equals("moto")) {
            veiculo = new Moto();
            veiculo.inserirDados();
        } else if(opcao.equals("carro")) {
            veiculo = new Carro();
            veiculo.inserirDados();
        }

        System.out.println("\nInformações do Veiculo: \n");
        veiculo.printDados();

        sc.close();

    }
}
