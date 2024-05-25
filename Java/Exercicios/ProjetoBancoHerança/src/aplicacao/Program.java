
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

import entidades.*;

public class Program {

	public static void main(String[] args) {

		Locale.setDefault(Locale.US);
		List<Conta> lista = new ArrayList<>();

		lista.add(new ContaPoupanca(1001, "Alex", 500.00, 0.01));
		lista.add(new Empresa(1002, "Maria", 1000.0, 400.0));
		lista.add(new ContaPoupanca(1004, "Bob", 300.0, 0.01));
		lista.add(new Empresa(1005, "Anna", 500.0, 500.0));

		for (Conta acc : lista) {
			System.out.printf("Saldo da conta %d: %.2f%n", acc.getNumero(), acc.getSaldo());
		}

		double soma = 0.0;
		for (Conta acc : lista) {
			soma += acc.getSaldo();
		}

		System.out.printf("Saldo total: %.2f%n", soma);

		for (Conta acc : lista) {
			acc.depositar(10.0);
		}

		for (Conta acc : lista) {
			System.out.printf("Saldo atualizado %d: %.2f%n", acc.getNumero(), acc.getSaldo());
		}

		soma = 0;

		for (Conta acc : lista) {

			soma += acc.getSaldo();
		}
		
		System.out.printf("Saldo total: %.2f%n", soma);
	}
}