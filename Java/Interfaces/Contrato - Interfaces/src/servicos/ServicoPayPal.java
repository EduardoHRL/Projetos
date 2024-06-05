package servicos;

public class ServicoPayPal implements ServicoPagamentoOnline {

    public double taxaPagamento(double valor) {
        return valor * 0.02;
    }

    public double juros(double valor, Integer meses) {
        return valor * 0.01 * meses;
    }
}
