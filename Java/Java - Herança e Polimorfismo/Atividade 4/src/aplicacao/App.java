package aplicacao;

import java.util.Scanner;
import entidades.*;;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Informe quantos funcionarios: ");
        int quant = sc.nextInt();

        Funcionario[] vetor = new Funcionario[quant];

        for(int i = 0; i < quant; i++) {
            System.out.println("\nDeseja cadastrar assalariado ou horista? (1 para assalariado ou 2 para horista): ");
            int opcao = sc.nextInt();

            if(1== opcao) {
                vetor[i] = new Assalariado();
                vetor[i].inserirDados();
            }
            else if (2 == opcao) {
                vetor[i] = new PorHora();
                vetor[i].inserirDados();
            }
        }

        for (Funcionario func : vetor) {
            if (func instanceof PorHora) {
                ((PorHora) func).addHoras(10);
            }
        }
        double total = 0;
        for (int i = 0;i < quant; i++) {
            total += vetor[i].receber();
        }

        System.out.println("ogasto total da empresa foi: "+total);
    }
}
