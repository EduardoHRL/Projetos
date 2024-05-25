package entidades;

//Criação da classe sendo abstract\\
public abstract class Contribuinte {
    //Variaveis\\
    private String nome;
    protected double renda;

    //Construtor Padrão\\
    public Contribuinte() {

    }

    //Construtor\\
    public Contribuinte(String nome, double renda) {
        this.nome = nome;
        this.renda = renda;
    }

    //Metodos gets e sets\\
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getRenda() {
        return renda;
    }

    public void setRenda(double renda) {
        this.renda = renda;
    }

    //Declaração do metodo Taxa e sendo abstract\\
    public abstract double Taxa();
}
