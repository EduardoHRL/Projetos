package Juros;

public class ServicoJuros implements ServicoJurosBrasil, ServicoJurosEua{

    public double taxaJurosBR() {
        return 1.02;
    }

    public double taxaJurosEua() {
        return 1.01;
    }

    public double pagamentoBr(double valor, int meses) {
        return valor * Math.pow(taxaJurosBR(), meses);
    }

    public double pagamentoEua(double valor, int meses) {
        return valor * Math.pow(taxaJurosEua(), meses);
    }
    
}
