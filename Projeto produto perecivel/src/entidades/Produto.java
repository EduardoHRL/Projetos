package entidades;

public class Produto {
    private String descricao;
    private String foto;
    protected double valor;
    private double quantidade;

    public Produto() {

    }

    public Produto(String descricao, double valor) {
        this.descricao = descricao;
        this.valor = valor;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public String getFoto() {
        return foto;
    }

    public void setFoto(String foto) {
        this.foto = foto;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(Double valor) {
        this.valor = valor;
    }

    public double getQuant() {
        return quantidade;
    }

    public void setQuant(double quant) {
        this.quantidade = quant;
    }
}