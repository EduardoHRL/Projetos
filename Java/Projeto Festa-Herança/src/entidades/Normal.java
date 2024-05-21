package entidades;

public class Normal extends Ingresso {
    public Normal() {
        super();
    }

    public Normal(double valor) {
        super(valor);
    }

    public void IngressoNormal(double valor) {
        System.out.printf("Ingresso normal: %.2f", valor);
    }
}
