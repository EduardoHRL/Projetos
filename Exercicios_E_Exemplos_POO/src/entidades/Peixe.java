package entidades;

public class Peixe extends Animal {

    private String caracteristica;

    public Peixe() {
        super();
    }

    public Peixe(String nome, double comprimento, int patas, String cor, String ambiente, double velocidade,
            String caracteristica) {
        super(nome, comprimento, patas, cor, ambiente, velocidade);
        this.caracteristica = caracteristica;
    }

    public String getCaracteristica() {
        return caracteristica;
    }

    public void setCaracteristica(String caracteristica) {
        this.caracteristica = caracteristica;
    }

    public void dadosPeixe() {
        System.out.print("\nNome: " + getNome());
        System.out.print("\nComprimento: " + getComprimento());
        System.out.print("\nPatas: " + getPatas());
        System.out.print("\nCor: " + getCor());
        System.out.print("\nAmbiente: " + getAmbiente());
        System.out.print("\nCaracteristica: " + caracteristica);
        System.out.print("\n");

    }

}
