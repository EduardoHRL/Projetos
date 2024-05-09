package entidades;
public class Cliente {
    private String nome;
    private String endereco;
    private Double renda;


    public Cliente(String nome, String endereco, double renda) {
        this.nome = nome;
        this.endereco = endereco;
        this.renda = renda;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEndereco() {
        return endereco;
    }
    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public double getRenda() {
        return renda;
    }
    public void setNome(double renda) {
        this.renda = renda;
    }

    public void EscreveDados(String nome, String endereco, Double renda) {
        System.out.printf("Nome: %s, Endereço: %s, Renda: %.2f", nome, endereco, renda);
    }
}