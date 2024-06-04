package entidades;

import java.time.LocalDateTime;

public class Contrato {
    private Integer numero;
    private LocalDateTime Data;
    private double valorTotal;
    
    public Contrato(Integer numero, LocalDateTime Data, double valorTotal) {
        this.numero = numero;
        this.Data = Data;
        this.valorTotal = valorTotal;
    }

    public Integer getNumero() {
        return numero;
    }

    public void setNumero(Integer numero) {
        this.numero = numero;
    }

    public LocalDateTime getData() {
        return Data;
    }

    public void setData(LocalDateTime data) {
        Data = data;
    }

    public double getValorTotal() {
        return valorTotal;
    }

    public void setValorTotal(double valorTotal) {
        this.valorTotal = valorTotal;
    }
    
}
