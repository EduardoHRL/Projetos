package entidades;

import java.time.LocalDateTime;

public class Prestacao {
    private double valor;
    private LocalDateTime dataVencimento;

    public Prestacao(LocalDateTime vencimento, double valor) {
        this.dataVencimento = vencimento;
        this.valor = valor;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public LocalDateTime getDataVencimento() {
        return dataVencimento;
    }

    public void setDataVencimento(LocalDateTime dataVencimento) {
        this.dataVencimento = dataVencimento;
    }

    
}
