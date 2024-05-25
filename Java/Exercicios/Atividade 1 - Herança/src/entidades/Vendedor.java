package entidades;

public class Vendedor extends Empregado{
    private double percentualComissao;

    public Vendedor() {
        super();
    }
    public Vendedor(String nome, double salario, double percentualComissao) {
        super(nome, salario);
        this.percentualComissao = percentualComissao;
    }

    public double calcularSalario() {
        salario += (salario * percentualComissao) / 100;
        return salario;
    }

    @Override
    public void dados() {
        System.out.print("\nNome: "+ getNome());
        System.out.print("\nSalário Antigo: "+ getSalario());
        System.out.print("\nSalário Atual: " + calcularSalario());
        System.out.print("\nPercentual de vendas: " + percentualComissao);
        System.out.print("\n");
    }
}
