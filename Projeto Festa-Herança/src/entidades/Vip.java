package entidades;

public class Vip extends Ingresso {
    private double valorAdicional;

    public Vip() {
        super();
    }

    public Vip(double valor, double valorAdicional) {
        super(valor);
        this.valorAdicional = valorAdicional;
    }

    public double getvalorAdicional() {
        return valorAdicional;
    }

    public void setvalorAdicional(double valorAdicional) {
        this.valorAdicional = valorAdicional;
    }

    public void setIngressoVip(double valor) {
        valor += valor + valorAdicional;
    }

    public void IngressoVip(double valor) {
        System.out.printf("Ingresso VIP: %.2f", valor);
    }
}
