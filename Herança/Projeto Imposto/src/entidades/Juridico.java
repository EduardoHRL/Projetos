package entidades;

public class Juridico extends Contribuinte{
    private int func;

    private Juridico() {
        super();
    }

    private Juridico(String nome, double renda, int func) {
        super(nome, renda);
        this.func = func;
    }

    public int getFunc() {
        return func;
    }

    public void setFunc(int func) {
        this.func = func;
    }
    
    
}
