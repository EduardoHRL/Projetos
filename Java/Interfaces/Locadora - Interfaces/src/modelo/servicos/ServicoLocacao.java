package modelo.servicos;

import java.time.Duration;

import modelo.entidades.Fatura;
import modelo.entidades.Locacao;

public class ServicoLocacao {
    private double precoPorHora;
    private double precoPorDia;

    private TaxaServico taxaServico;

    public ServicoLocacao(double precoPorHora, double precoPorDia, TaxaServico taxaservico) {
        this.precoPorHora = precoPorHora;
        this.precoPorDia = precoPorDia;
        this.taxaServico = taxaservico;
    }

    public void processoFatura(Locacao locacao) {
        double minutos = Duration.between(locacao.getRetirada(),locacao.getRetorno()).toMinutes();
        double horas = minutos / 60;
        double pagamentoBasico;

        if (horas < 12) {
            pagamentoBasico = precoPorHora * Math.ceil(horas);

        }
        else {
            pagamentoBasico = precoPorDia * Math.ceil(horas / 24);
        }

        double taxa = taxaServico.taxa(pagamentoBasico);

        locacao.setFatura(new Fatura(pagamentoBasico, taxa));
    }
    
}
