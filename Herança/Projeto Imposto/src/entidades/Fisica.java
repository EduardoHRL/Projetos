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
    public void Taxa() {
        if (renda < 20000) {
            
        }
    }
    
}
