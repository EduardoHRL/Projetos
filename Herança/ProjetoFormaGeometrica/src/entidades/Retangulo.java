package entidades;

import entidades.enums.Cor;

public class Retangulo extends Forma {
    private double altura;
    private double largura;

    public Retangulo() {
        super();
    }

    public Retangulo(double altura, double largura, Cor cor) {
        super(cor);
        this.altura = altura;
        this.largura = largura;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public double getLargura() {
        return largura;
    }

    public void setLargura(double largura) {
        this.largura = largura;
    }

    @Override
    public double area() {
        return altura * largura;
    }

}
