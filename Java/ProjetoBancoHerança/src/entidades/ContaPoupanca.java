package entidades;

public class ContaPoupanca extends Conta{
    private double juros;

    
    public ContaPoupanca() {
        super();
    }

    public ContaPoupanca(int numero, String titular, double saldo, double juros) {
        super(numero, titular, saldo);
        this.juros = juros;
    }

    public double getJuros() {
        return juros;
    }

    public void setJuros(double juros) {
        this.juros = juros;
    }

    public void alterarSaldo() {
        saldo += saldo * juros;
    }

    @Override
    public void sacar(double valor) {
        super.sacar(valor);
        saldo -= 2.0;
    }
}
