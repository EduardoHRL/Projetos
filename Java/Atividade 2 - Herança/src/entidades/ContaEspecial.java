package entidades;

public class ContaEspecial extends ContaCorrente {
    private double limite;

    public ContaEspecial() {
        super();
    }

    public ContaEspecial(String nome, double saldo, double limite) {
        super(nome, saldo);
        this.limite = limite;
    }

    public double getLimite() {
        return limite;
    }

    public void setLimite(double limite) {
        this.limite = limite;
    }

    public boolean sacar(double valor) {
        if (valor < limite) {
            saldo -= valor;
            return true;
        } else {
            return false;
        }
    }

    public void dados() {
        System.out.print("\nNome: " + getNome());
        System.out.print("\nSaldo: " + saldo);
        System.out.print("\nLimite: " + getLimite());
        System.out.print("\n");
    }

}
