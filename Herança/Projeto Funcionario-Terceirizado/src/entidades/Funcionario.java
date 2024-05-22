package entidades;

public class Funcionario {
    
    private String nome;
	private int horas;
	private Double valorPorHora;

	public Funcionario() {
		
	}

	public Funcionario(String nome, int horas, Double valorPorHora) {
		this.nome = nome;
		this.horas = horas;
		this.valorPorHora = valorPorHora;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getHoras() {
		return horas;
	}

	public void setHoras(int horas) {
		this.horas = horas;
	}

	public Double getValorPorHora() {
		return valorPorHora;
	}

	public void setValorPorHora(Double valorPorHora) {
		this.valorPorHora = valorPorHora;
	}

	public double pagamento() {
		return horas * valorPorHora;
	}

}
