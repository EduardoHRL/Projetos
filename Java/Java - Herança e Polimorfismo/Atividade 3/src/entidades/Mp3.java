package entidades;

import java.util.Scanner;

public class Mp3 extends Arquivo {
    private int nDownloads;

    public Mp3() {
        super();
    }

    public Mp3(String autor, double preco, int kbytes, int nDownloads) {
        super(autor, preco, kbytes);
        this.nDownloads = nDownloads;
    }

    public int getnDownloads() {
        return nDownloads;
    }

    public void setnDownloads(int nDownloads) {
        this.nDownloads = (nDownloads > 0) ? nDownloads : 0;
    }

    public void reajuste() {
        if (nDownloads > 5000) {
            preco += preco * 5 / 100;
        }
    }

    @Override
    public String tipo() {
        return "Mp3: ";
    }

    @Override
    public String detalhes() {
        return super.detalhes() +
        "\nNúmeros de downloads: " + nDownloads;
    }


    @Override
    public void insereDados() {
        Scanner sc = new Scanner(System.in);
        super.insereDados();

        System.out.println(" Entre com o número de downloads: ");
        int nDownloads = sc.nextInt();

        this.nDownloads = nDownloads;
    }

}
