package entidades;

public class Nokia {
    private String nome;
    private String marca;
    private String sistemaOperacional;
    private String cor;
    private String tipoTela;
    private String tipoBateria;
    private int capacidadeBateria;
    private int memoriaRam;
    private int armazenamento;
    private String chip;

    public Nokia() {

    }

    public Nokia(String nome, String marca, String sistemaOperacional, String cor, String tipoBateria,
            int capacidadeBateria, int memoriaRam, int armazenamento, String tipoTela, String chip) {
        this.nome = nome;
        this.marca = marca;
        this.sistemaOperacional = sistemaOperacional;
        this.cor = cor;
        this.tipoBateria = tipoBateria;
        this.capacidadeBateria = capacidadeBateria;
        this.memoriaRam = memoriaRam;
        this.armazenamento = armazenamento;
        this.tipoTela = tipoTela;
        this.chip = chip;
    }

    public String getChip() {
        return chip;
    }

    public void setChip(String chip) {
        this.chip = chip;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getSistemaOperacional() {
        return sistemaOperacional;
    }

    public void setSistemaOperacional(String sistemaOperacional) {
        this.sistemaOperacional = sistemaOperacional;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getTipoBateria() {
        return tipoBateria;
    }

    public void setTipoBateria(String tipoBateria) {
        this.tipoBateria = tipoBateria;
    }

    public int getCapacidadeBateria() {
        return capacidadeBateria;
    }

    public void setCapacidadeBateria(int capacidadeBateria) {
        this.capacidadeBateria = capacidadeBateria;
    }

    public int getMemoriaRam() {
        return memoriaRam;
    }

    public void setMemoriaRam(int memoriaRam) {
        this.memoriaRam = memoriaRam;
    }

    public int getArmazenamento() {
        return armazenamento;
    }

    public void setArmazenamento(int armazenamento) {
        this.armazenamento = armazenamento;
    }

    public String getTela() {
        return tipoTela;
    }

    public void setTela(String tipoTela) {
        this.tipoTela = tipoTela;
    }
}