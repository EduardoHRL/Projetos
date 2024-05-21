package entidades;

public class CamaroteInferior extends Vip{

    private String localizacao;

    public CamaroteInferior() {
        super();
    }

    public CamaroteInferior(String localizacao) {
        this.localizacao = localizacao;
    }

    public String getLocalizacao() {
        return localizacao;
    }

    public void setLocalizacao(String localizacao) {
        this.localizacao = localizacao;
    }

    public void valorNormal(double valor, double valorAdicional) {
        valor -= valorAdicional;
    }

    public void Localizacao(double valor) {
        System.out.printf("O ingresso fica em %s e custa %.2f",localizacao, valor);
    }


    
}
