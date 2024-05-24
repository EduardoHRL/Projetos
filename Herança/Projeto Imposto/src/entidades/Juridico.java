package entidades;

public class Juridico extends Contribuinte{
    private int func;

    public Juridico() {
        super();
    }

    public Juridico(String nome, double renda, int func) {
        super(nome, renda);
        this.func = func;
    }

    public int getFunc() {
        return func;
    }

    public void setFunc(int func) {
        this.func = func;
    }

    @Override
	public double Taxa() {
		if (func > 10) {
			return renda * 0.14;
		}
		else {
			return renda * 0.16;
		}
	}
    
    
}
