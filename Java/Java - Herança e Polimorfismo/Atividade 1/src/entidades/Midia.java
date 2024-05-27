package entidades;

import java.util.Scanner;

public abstract class Midia {
    private int codigo;
    private String nome;
    private double preco;

    public Midia() {

    }

    public Midia(int codigo, String nome, double preco) {
        this.codigo = codigo;
        this.nome = nome;
        this.preco = preco;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public String tipo() {
        return "Midia: ";
    }

    public String detalhes() {
        return "Codigo: " + codigo
                + "\nNome: " + nome
                + "\nPreço: " + preco;
    }

    public void printDados() {
        String s = tipo() + "\n" + detalhes() + "\n";
        System.out.println(s);
    }

    public void insereDados() {
        Scanner sc = new Scanner(System.in);

        System.out.printf("\n Entre com o codigo: ");
        int codigo = sc.nextInt();
        sc.nextLine();
        System.out.printf("\n Entre com o nome: ");
        String nome = sc.nextLine();
        System.out.printf("\n Entre com o preco: ");
        double preco = sc.nextDouble();
 
        this.nome = nome;
        this.preco = preco;
        this.codigo = codigo;


    }
}
