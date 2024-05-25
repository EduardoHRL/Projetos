package entidades;

//Criação da classe herdando de Contribuinte\\
public class Fisica extends Contribuinte{
    private double gastos;

    //Construtor padrão com o metodo super()\\
    public Fisica() {
        super();
    }
    //Construtor com as variais da classe e as herdadas\\
    public Fisica(String nome, double renda, double gastos) {
        super(nome, renda);
        this.gastos = gastos;
    }
    
    //Metodos gets e sets\\
    public double getGastos() {
        return gastos;
    }
    public void setGastos(double gastos) {
        this.gastos = gastos;
    }
    
    //Sobreposição do metodo taxa\\
    @Override
    public double Taxa() {
        //Condição para retornar a renda com determinada quantidade de imposto de acordo com a renda\\
        if (renda < 20000.0) {
			return renda * 0.15 - gastos * 0.5;
		}
		else {
			return renda * 0.25 - gastos * 0.5;
		}
	}
    
    
}
