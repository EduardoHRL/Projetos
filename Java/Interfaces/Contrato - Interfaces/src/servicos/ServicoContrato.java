package servicos;

import entidades.Contrato;
import entidades.Prestacao;

import java.time.LocalDate;

public class ServicoContrato {
    private double valorTotal = 0;

    private ServicoPagamentoOnline servicoPagamentoOnline;

    public ServicoContrato(ServicoPagamentoOnline servicoPagamentoOnline) {
        this.servicoPagamentoOnline = servicoPagamentoOnline;
    }

    public void processoContrato(Contrato contrato, int meses) {
        double quotaBasica = contrato.getValorTotal() / meses;

        for (int i = 1; i <= meses; i++) {
            LocalDate dataParcela = contrato.getData().plusMonths(i);
            double juros = servicoPagamentoOnline.juros(quotaBasica, i);
            double taxa = servicoPagamentoOnline.taxaPagamento(quotaBasica + juros);
            double quota = quotaBasica + juros + taxa;
            contrato.getPrestacao().add(new Prestacao(dataParcela, quota, valorTotal));
            valorTotal += quota;
        }
        this.valorTotal = valorTotal;
    }
    public double getValorTotal() {
        return valorTotal;
    }
}
