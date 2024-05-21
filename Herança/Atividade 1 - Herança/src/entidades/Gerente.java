package entidades;

public class Gerente extends Empregado{
    private String departamento;

    public Gerente() {
        super();
    }

    public Gerente(String nome, double salario, String departamento) {
        super(nome, salario);
        this.departamento = departamento;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    @Override
    public void dados() {
        System.out.print("\nDepartamento: " + departamento);
        System.out.print("\nNome: " + getNome());
        System.out.print("\nSalário: " + salario);
        System.out.print("\n");
    }
    
}
