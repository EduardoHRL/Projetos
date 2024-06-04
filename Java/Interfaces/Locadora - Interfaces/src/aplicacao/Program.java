package aplicacao;

import java.text.ParseException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

import modelo.entidades.Locacao;
import modelo.entidades.Veiculo;
import modelo.servicos.BrasilTaxaServico;
import modelo.servicos.ServicoLocacao;

public class Program {

	public static void main(String[] args) throws ParseException {

		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		DateTimeFormatter fmt =  DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
		
		System.out.println("Entre com os dados do aluguel");
		System.out.print("Modelo do carro: ");
		String carModel = sc.nextLine();
		System.out.print("Retirada (dd/MM/yyyy HH:mm): ");
		LocalDateTime start = LocalDateTime.parse(sc.nextLine(), fmt);
		System.out.print("Retorno (dd/MM/yyyy HH:mm): ");
		LocalDateTime finish = LocalDateTime.parse(sc.nextLine(), fmt);
		
		Locacao cr = new Locacao(start, finish, new Veiculo(carModel));

		System.out.print("Entre com o preço por hora: ");
		double pricePerHour = sc.nextDouble();
		System.out.print("Entre com o preço por dia: ");
		double pricePerDay = sc.nextDouble();
		
		ServicoLocacao rentalService = new ServicoLocacao(pricePerDay, pricePerHour, new BrasilTaxaServico());
		
		rentalService.processoFatura(cr);

		System.out.println("FATURA:");
		System.out.println("Pagamento basico: " + String.format("%.2f", cr.getFatura().getPagamentoBasico()));
		System.out.println("Imposto: " + String.format("%.2f", cr.getFatura().getTaxa()));
		System.out.println("Pagamento total: " + String.format("%.2f", cr.getFatura().getPagamentoTotal()));
		
		sc.close();
	}
}