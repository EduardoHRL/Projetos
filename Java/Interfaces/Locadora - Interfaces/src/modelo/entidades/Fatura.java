package modelo.entidades;

public class Fatura {
    private double pagamentoBasico;
    private double taxa;

    public Fatura() {

    }
    public Fatura(double pagamentoBasico, double taxa) {
        this.pagamentoBasico = pagamentoBasico;
        this.taxa = taxa;
    }
    public double getPagamentoBasico() {
        return pagamentoBasico;
    }
    public void setPagamentoBasico(double pagamentoBasico) {
        this.pagamentoBasico = pagamentoBasico;
    }
    public double getTaxa() {
        return taxa;
    }
    public void setTaxa(double taxa) {
        this.taxa = taxa;
    }

    public double getPagamentoTotal() {
        return getPagamentoBasico() + getTaxa();
    }
}
