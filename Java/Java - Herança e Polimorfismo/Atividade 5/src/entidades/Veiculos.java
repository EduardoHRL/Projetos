package entidades;

import java.util.Scanner;

public abstract class Veiculos {
    private String modelo;
    protected double preco;

    public Veiculos() {
    }

    public Veiculos(String modelo, double preco) {
        this.modelo = modelo;
        this.preco = preco;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public void printDados() {
        System.out.println("Modelo: " + modelo);
        System.out.println("Preço: " + preco);
    }

    public void inserirDados() {
        Scanner sc = new Scanner(System.in);

        System.out.printf(" Informe o modelo da moto: ");
        String modelo = sc.nextLine();
        System.out.printf(" Informe o preço da moto: ");
        double preco = sc.nextDouble();

        this.modelo = modelo;
        this.preco = preco;
    }

}
