package entidades;

public class CamaroteSuperior extends Vip{

    private String localizacao;

    public CamaroteSuperior() {
        super();
    }

    public CamaroteSuperior(double valor, double valorAdicional, String localizacao) {
        super(valor, valorAdicional);
        this.localizacao = localizacao;
    }

    public String getLocalizacao() {
        return localizacao;
    }

    public void setLocalizacao(String localizacao) {
        this.localizacao = localizacao;
    }

    public void Localizacao(double valor) {
        System.out.printf("O ingresso fica no %s e custa %.2f",localizacao, valor);
    }
}
