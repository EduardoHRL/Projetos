package entidades;

public class Iphone extends Nokia {
    private String resistenteAgua;
    private String deteccaoFacial;
    private String slowMotion;
    private String NFC;
    private String zoomOptico;

    public Iphone() {
        super();
    }

    public Iphone(String nome, double preco, String marca, String sistemaOperacional, String cor, String tipoBateria,
            int capacidadeBateria, int memoriaRam, int armazenamento, String tipoTela, int numero,
            String resistenteAgua, String deteccaoFacial, String slowMotion, String nFC, String zoomOptico) {
        super(nome, preco, marca, sistemaOperacional, cor, tipoBateria, capacidadeBateria, memoriaRam, armazenamento,
                tipoTela, numero);
        this.resistenteAgua = resistenteAgua;
        this.deteccaoFacial = deteccaoFacial;
        this.slowMotion = slowMotion;
        NFC = nFC;
        this.zoomOptico = zoomOptico;
    }

    public String getResistenteAgua() {
        return resistenteAgua;
    }

    public void setResistenteAgua(String resistenteAgua) {
        this.resistenteAgua = resistenteAgua;
    }

    public String getDeteccaoFacial() {
        return deteccaoFacial;
    }

    public void setDeteccaoFacial(String deteccaoFacial) {
        this.deteccaoFacial = deteccaoFacial;
    }

    public String getSlowMotion() {
        return slowMotion;
    }

    public void setSlowMotion(String slowMotion) {
        this.slowMotion = slowMotion;
    }

    public String getNFC() {
        return NFC;
    }

    public void setNFC(String nFC) {
        NFC = nFC;
    }

    public String getZoomOptico() {
        return zoomOptico;
    }

    public void setZoomOptico(String zoomOptico) {
        this.zoomOptico = zoomOptico;
    }

    public void pagarComNFC() {
        System.out.println("Ligando o NFC...");
        System.out.println("Compra sendo processada...");
        System.out.println("Concluido!");
    }
}
