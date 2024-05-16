package entidades;

public class Mamifero extends Animal {
    private String alimento;

    public Mamifero() {
        super();
    }

    public Mamifero(String nome, double comprimento, int patas, String cor, String ambiente, double velocidade,
            String alimento) {
        super(nome, comprimento, patas, cor, ambiente, velocidade);
        this.alimento = alimento;
    }

    public String getAlimento() {
        return alimento;
    }
    public void setAlimento(String alimento) {
        this.alimento = alimento;
    }

    public void dadosMamifero() {
        System.out.print("\nNome: " + getNome());
        System.out.print("\nComprimento: " + getComprimento());
        System.out.print("\nPatas: " + getPatas());
        System.out.print("\nCor: " + getCor());
        System.out.print("\nAmbiente: " + getAmbiente());
        System.out.print("\nAlimento: " + alimento);
        System.out.printf("\n");
    }
}
