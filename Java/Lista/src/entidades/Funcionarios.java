package entidades;

public class Funcionarios {

    private int id;
    private String nome;
    private double salario;

    public Funcionarios(int id, String nome, double salario) {
        setId(id);
        setNome(nome);
        setSalario(salario);
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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

    public void AlteraSalario(double porcentagem) {
        salario = (salario * porcentagem) / 100;
    }

    public String toString() {
        return + id
        +", "
        + nome
        + ", "
        +salario;
    }

}
