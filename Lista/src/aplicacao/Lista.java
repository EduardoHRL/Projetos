package aplicacao;

import java.util.Locale;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.ArrayList;
import java.util.List;

public class Lista {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

		List<String> lista = new ArrayList<>();
		
		lista.add("Maria");
		lista.add("Alex");
		lista.add("Bob");
		lista.add("Anna");
		lista.add(2, "Marco");
		
		System.out.println(lista.size());
		
		for (String x : lista) {
			System.out.println(x);
		}
		System.out.println("---------------------");
		lista.removeIf(x -> x.charAt(0) == 'M');
		
		for (String x : lista) {
			System.out.println(x);
		}
		System.out.println("---------------------");
		System.out.println("Index of Bob: " + lista.indexOf("Bob"));
		System.out.println("Index of Marco: " + lista.indexOf("Marco"));
		System.out.println("Index of Alex: " + lista.indexOf("Alex"));
		System.out.println("Index of Anna: " + lista.indexOf("Anna"));
		System.out.println("---------------------");
		
		List<String> result = lista.stream().filter(x -> x.charAt(0) == 'A').collect(Collectors.toList());
		
		for (String x : result) {
			System.out.println(x);
		}
		
		System.out.println("---------------------");
		
		String name = lista.stream().filter(x -> x.charAt(0) == 'J').findFirst().orElse(null);
		System.out.println(name);
		sc.close();
	}

    }
