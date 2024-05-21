package entidades;

public class Empresa extends Conta{
    private double limiteEmprestimo;

    public Empresa() {
        super();
    }

    public Empresa(int numero, String titular, double saldo, double limiteEmprestimo) {
        super(numero, titular, saldo);
        this.limiteEmprestimo = limiteEmprestimo;
    }

    public double getlimiteEmprestimo() {
        return limiteEmprestimo;
    }

    public void setlimiteEmprestimo(double limite) {
        limiteEmprestimo = limite;
    }

    public void emprestimo(double valor) {
        if (valor <= limiteEmprestimo) {
            saldo += valor - 10;
        }
    }
    
}
