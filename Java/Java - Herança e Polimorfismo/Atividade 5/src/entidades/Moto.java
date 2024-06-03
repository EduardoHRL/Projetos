package entidades;

import java.util.Scanner;

public class Moto extends Veiculos {
    private int ano;

    public Moto() {
        super();
    }

    public Moto(String modelo, double preco, int ano) {
        super(modelo, preco);
        this.ano = ano;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public double getPreco() {
        return preco;
    }
    @Override
    public void printDados() {
        super.printDados();
        System.out.println("Ano da moto: "+ ano);
    }

    @Override
    public void inserirDados() {
        Scanner sc = new Scanner(System.in);

        System.out.printf(" Informe o ano da moto: ");
        int ano = sc.nextInt();
        super.inserirDados();
        
        this.ano = ano;
    }

}
