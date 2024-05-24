package entidades;

public class Fisica extends Contribuinte{
    private double gastos;

    public Fisica() {
        super();
    }
    public Fisica(String nome, double renda, double gastos) {
        super(nome, renda);
        this.gastos = gastos;
    }
    public double getGastos() {
        return gastos;
    }
    public void setGastos(double gastos) {
        this.gastos = gastos;
    }
    
    @Override
    public double Taxa() {
        if (renda < 20000.0) {
			return renda * 0.15 - gastos * 0.5;
		}
		else {
			return renda * 0.25 - gastos * 0.5;
		}
	}
    
    
}
