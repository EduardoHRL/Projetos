package entidades;

public class ContaCorrente extends Cliente {
    protected double saldo;

    public ContaCorrente() {
        super();
    }

    public ContaCorrente(String nome, double saldo) {
        super(nome);
        this.saldo = saldo;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double valor) {
        saldo += saldo + valor;
    }

    public boolean sacar(double valor) {
        if (saldo >= valor) {
            saldo -= valor;
            return true;
        } else {
            return false;
        }
    }

    public void dados() {
        System.out.print("\nNome: " + getNome());
        System.out.print("\nSaldo: " + saldo);
    }

    public boolean transferir(ContaCorrente conta, double valor) {
        if (valor <= 0 || saldo < valor) {
            return false;
        }
        saldo -= valor;
        conta.saldo += valor;

        return true;
    }
}
