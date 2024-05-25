package entidades;

public class FuncionarioTerceirizado extends Funcionario{

    private double pagamentoAdicional;

    public FuncionarioTerceirizado() {
        super();
    }
    
    public FuncionarioTerceirizado(String nome, int horas, Double valorPorHora, double pagamentoAdicional) {
        super(nome, horas, valorPorHora);
        this.pagamentoAdicional = pagamentoAdicional;
    }

    public double getPagamentoAdicional() {
        return pagamentoAdicional;
    }

    public void setPagamentoAdicional(double pagamentoAdicional) {
        this.pagamentoAdicional = pagamentoAdicional;
    }

    @Override
	public double pagamento() {
		return super.pagamento() + pagamentoAdicional * 1.1;
	}

}
