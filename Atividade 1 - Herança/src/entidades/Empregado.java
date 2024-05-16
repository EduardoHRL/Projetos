package entidades;

public class Empregado {
    private String nome;
    protected double salario;

    public Empregado() {

    }
    public Empregado(String nome, double salario) {
        this.nome = nome;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public void dados() {
        System.out.print("\nNome: "+ nome);
        System.out.print("\nSalario: "+ salario);
        System.out.print("\n");
    }

}
