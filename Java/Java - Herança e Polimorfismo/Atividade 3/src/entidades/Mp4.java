package entidades;

import java.util.Scanner;

public class Mp4 extends Arquivo {
    private int nVisitas;

    public Mp4() {
        super();
    }

    public Mp4(String autor, double preco, int kbytes, int nVisitas) {
        super(autor, preco, kbytes);
        this.nVisitas = nVisitas;
    }

    public int getnVisitas() {
        return nVisitas;
    }

    public void setnVisitas(int nVisitas) {
        this.nVisitas = (nVisitas > 0) ? nVisitas : 0;
    }

    public void reajuste() {
        if (nVisitas > 10000) {
            preco += preco * 8 / 100;
        }
    }

    @Override
    public String tipo() {
        return "Mp4: ";
    }

    @Override
    public String detalhes() {
        return super.detalhes()
        +"\nNúmero de visitas: " + nVisitas;
    }

    @Override
    public void insereDados() {
        Scanner sc = new Scanner(System.in);
        super.insereDados();

        System.out.println(" Entre com o número de visualizações: ");
        int nVisitas = sc.nextInt();

        this.nVisitas = nVisitas;
    }

}
