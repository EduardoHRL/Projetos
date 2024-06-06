package entidades;

public class Emprestimo {
    private double quantia;
    private int meses;

    public Emprestimo(double quantia, int meses) {
        this.quantia = quantia;
        this.meses = meses;
    }

    public double getQuantia() {
        return quantia;
    }

    public void setQuantia(double quantia) {
        this.quantia = quantia;
    }

    public int getMeses() {
        return meses;
    }

    public void setMeses(int meses) {
        this.meses = meses;
    }
}
