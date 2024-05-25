package entidades;

public class Produto {
    private String nome;
    private double preco;

    public Produto() {

    }

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
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
    
    public void tagPreco() {
        System.out.printf("Nome: %s", getNome());
        System.out.printf("Preço: %.2f", getPreco());
    }
}
