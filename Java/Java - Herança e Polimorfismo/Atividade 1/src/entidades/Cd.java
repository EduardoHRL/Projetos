package entidades;
import java.util.Scanner;

public class Cd extends Midia{
    private int nMusicas;

    public Cd() {
        super();
    }

    public Cd(int codigo, String nome, double preco, int nMusicas) {
        super(codigo, nome, preco);
        this.nMusicas = nMusicas;
    }

    public int getnMusicas() {
        return nMusicas;
    }

    public void setnMusicas(int nMusicas) {
        this.nMusicas = nMusicas;
    }

    @Override
    public String tipo() {
        return "Cd: ";
    }

    @Override
    public String detalhes() {
        return super.detalhes()
        +"\nNúmeros de músicas: " + nMusicas;
    }

    @Override
    public void insereDados() {
        super.insereDados();
        Scanner sc = new Scanner(System.in);


        System.out.printf("\n Entre com o número de Musicas: ");
        int musicas = sc.nextInt();

        this.nMusicas = musicas;

    }
    
}
