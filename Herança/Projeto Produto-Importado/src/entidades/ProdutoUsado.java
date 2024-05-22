package entidades;

import java.util.Date;

public class ProdutoUsado extends Produto {
    private Date dataFabricacao;

    public ProdutoUsado() {
        super();
    }

    public ProdutoUsado(String nome, double preco, Date dataFabricacao) {
        super(nome, preco);
        this.dataFabricacao = dataFabricacao;
    }

    public Date getDataFabricacao() {
        return dataFabricacao;
    }

    public void setDataFabricacao(Date dataFabricacao) {
        this.dataFabricacao = dataFabricacao;
    }

    @Override
    public void tagPreco() {
        System.out.printf("Nome: %s", getNome());
        System.out.printf("Preço: %.2f", getPreco());
        System.out.printf("Data de Fabricação: %d")
    }
}
