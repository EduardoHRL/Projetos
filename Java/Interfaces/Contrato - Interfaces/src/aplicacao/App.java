package aplicacao;

import entidades.Contrato;
import servicos.ServicoContrato;
import servicos.ServicoPayPal;
import entidades.Prestacao;

import java.util.Scanner;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        double total = 0;
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println("Entre com os dados do contrato:");

        System.out.printf("Número: ");
        int numero = sc.nextInt();
        sc.nextLine();

        System.out.printf("Data: ");
        String dataS = sc.nextLine();
        LocalDate data = LocalDate.parse(dataS, fmt);

        System.out.printf("Valor do contrato: ");
        double valor = sc.nextDouble();

        Contrato contrato = new Contrato(numero, data, valor);

        System.out.printf("Quantidade de parcelas: ");
        int quant = sc.nextInt();

        ServicoContrato serc = new ServicoContrato(new ServicoPayPal());

        serc.processoContrato(contrato, quant);

        System.out.println("Parcelas:");
        for (Prestacao prestacao : contrato.getPrestacao()) {
            System.out.println(prestacao);
            
        }



        sc.close();

    }
}
