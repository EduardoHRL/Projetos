package servicos;

public interface ServicoPagamentoOnline {
    double taxaPagamento(double valor);

    double juros(double valor, Integer meses);
}
