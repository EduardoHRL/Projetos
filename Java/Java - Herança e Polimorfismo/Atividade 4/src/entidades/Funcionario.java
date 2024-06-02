package entidades;

public abstract class Funcionario {
    protected String nome;

    public Funcionario() {

    }

    public Funcionario(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public abstract double receber();

    public void mostrarPagamento() {
        System.out.println("Salario do funcionario " + nome +": " +receber());
    }

    public abstract void inserirDados();

}
