package entidades;

import java.util.Scanner;

public class Carro extends Veiculos {
    private double km;

    public Carro() {
        super();
    }

    public Carro(String modelo, double preco, double km) {
        super(modelo, preco);
        this.km = km;
    }

    public double getKm() {
        return km;
    }

    public void setKm(double km) {
        this.km = km;
    }

    public double getPreco() {
        return preco;
    }
    @Override
    public void printDados() {
        super.printDados();
        System.out.println("Km rodados: "+ km);
    }

    @Override
    public void inserirDados() {
        Scanner sc = new Scanner(System.in);

        super.inserirDados();

        System.out.printf(" Informe os KM rodados: ");
        double km = sc.nextDouble();

        this.km = km;
    }

}
