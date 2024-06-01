package entidades;

import java.util.Scanner;

public abstract class Arquivo {
    private int kbytes;
    protected double preco;
    private String autor;

    public Arquivo() {

    }

    public Arquivo(String autor, double preco, int kybtes) {
        this.autor = autor;
        this.preco = preco;
        this.kbytes = kybtes;
    }

    public int getKbytes() {
        return kbytes;
    }

    public void setKbytes(int kbytes) {
        this.kbytes = kbytes;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    } 

    public String tipo() {
        return "Arquivo: ";
    }

    public String detalhes() {
        return "Autor: " +autor
        +"\nPreco: " +preco
        +"\nTamanho do arquivo: " +kbytes;
    }

    public void printDados() {
        String s = tipo() + "\n" + detalhes() + "\n";
        System.out.println(s);
    }

    public void insereDados() {
        Scanner sc = new Scanner(System.in);

        System.out.printf("\n Entre com o autor: ");
        String autor = sc.nextLine();
        System.out.println("\n Entre com o preço: ");
        double preco = sc.nextDouble();
        System.out.println("\n Entre com o tamanho do arquivo: ");
        int kbytes = sc.nextInt();

        this.autor = autor;
        this.preco = preco;
        this.kbytes = kbytes;
    }
}
