package entidades;

//Criação da classe herdando de Contribuinte\\
public class Juridico extends Contribuinte{
    private int func;

    //Construtor padrão com o metodo super()\\
    public Juridico() {
        super();
    }

    //Construtor com as variaveis da classe e as herdadas\\
    public Juridico(String nome, double renda, int func) {
        super(nome, renda);
        this.func = func;
    }

    //Metodos gets e sets\\
    public int getFunc() {
        return func;
    }

    public void setFunc(int func) {
        this.func = func;
    }

    //Sobreposição do metodo Taxa\\
    @Override
	public double Taxa() {
        //Condição para retornar a renda multiplicada por uma quantidade de impostos de acordo com a quantidade de funcionarios\\
		if (func > 10) {
			return renda * 0.14;
		}
		else {
			return renda * 0.16;
		}
	}
    
    
}
