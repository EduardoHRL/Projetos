package entidades;

import java.time.LocalDate;
import java.util.List;
import java.util.ArrayList;

public class Contrato {
    private Integer numero;
    private LocalDate Data;
    private double valorTotal;

    private List<Prestacao> prestacao = new ArrayList<>();
    
    public Contrato(Integer numero, LocalDate Data, double valorTotal) {
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

    public LocalDate getData() {
        return Data;
    }

    public void setData(LocalDate data) {
        Data = data;
    }

    public double getValorTotal() {
        return valorTotal;
    }

    public void setValorTotal(double valorTotal) {
        this.valorTotal = valorTotal;
    }

    public List<Prestacao> getPrestacao() {
        return prestacao;
    }
    
}
