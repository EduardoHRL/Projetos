package aplicacao;

import java.util.Scanner;

import entidades.*;

import Juros.ServicoJuros;

public class Programa {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Informe o valor do emprestimo: ");
        double valor = sc.nextDouble();

        System.out.println("Informe a quantidade de meses: ");
        int meses = sc.nextInt();

        Emprestimo emprestimo = new Emprestimo(valor, meses);

        ServicoJuros pagamento = new ServicoJuros();

        System.out.printf("Pagamentos após %d meses no Brasil é de %.2f",meses,pagamento.pagamentoBr(valor, meses));
        System.out.printf("\nPagamentos após %d meses nos Estados Unidos é de %.2f", meses, pagamento.pagamentoEua(valor, meses));
    }

}