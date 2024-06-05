package entidades;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Prestacao {
    private double valor;
    private LocalDate dataVencimento;
    private double valorTotal;

    private static DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");

    public Prestacao(LocalDate vencimento, double valor, double valorTotal) {
        this.dataVencimento = vencimento;
        this.valor = valor;
        this.valorTotal = valorTotal;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public LocalDate getDataVencimento() {
        return dataVencimento;
    }

    public void setDataVencimento(LocalDate dataVencimento) {
        this.dataVencimento = dataVencimento;
    }

    public double getValorTotal() {
        return valorTotal;
    }

    public void setValorTotal(double valorTotal) {
        this.valorTotal = valorTotal;
    }
    public String toString() {
    return dataVencimento.format(fmt) +" - " + String.format("%.2f", valor, valorTotal);
    }
    
}
