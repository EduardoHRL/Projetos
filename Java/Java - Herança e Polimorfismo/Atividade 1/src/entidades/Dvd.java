package entidades;

public class Dvd extends Midia {
    private int nFaixas;

    public Dvd() {
        super();
    }

    public Dvd(int codigo, String nome, double preco, int nFaixas) {
        super(codigo, nome, preco);
        this.nFaixas = nFaixas;
    }

    public int getnFaixas() {
        return nFaixas;
    }

    public void setnFaixas(int nFaixas) {
        this.nFaixas = nFaixas;
    }

    @Override
    public String tipo() {
        return ("Dvd: ");
    }

    @Override
    public String detalhes() {
        return super.detalhes() 
        +"\nNúmero de faixas: " +nFaixas;
    }
}
