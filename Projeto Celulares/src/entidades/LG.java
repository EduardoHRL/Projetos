package entidades;

public class LG extends Nokia {
    private String internet;
    private String camera;
    private String flash;
    private String bluetooth;
    private String impressaoDigital;
    private String infraVermelho;
    private String memoriaExpansivel;
    private String sensores;

    public LG() {
        super();
    }

    public LG(String nome, String marca, String sistemaOperacional, String cor, String tipoBateria,
            int capacidadeBateria, int memoriaRam, int armazenamento, String tipoTela, String chip, String internet,
            String camera, String flash, String bluetooth, String impressaoDigital,
            String infraVermelho, String memoriaExpansivel, String sensores) {
        super(nome, marca, sistemaOperacional, cor, tipoBateria, capacidadeBateria, memoriaRam, armazenamento, tipoTela,
                chip);
        this.internet = internet;
        this.camera = camera;
        this.flash = flash;
        this.bluetooth = bluetooth;
        this.impressaoDigital = impressaoDigital;
        this.infraVermelho = infraVermelho;
        this.memoriaExpansivel = memoriaExpansivel;
        this.sensores = sensores;
    }

    public String getInternet() {
        return internet;
    }

    public void setInternet(String internet) {
        this.internet = internet;
    }

    public String getCamera() {
        return camera;
    }

    public void setCamera(String camera) {
        this.camera = camera;
    }

    public String getFlash() {
        return flash;
    }

    public void setFlash(String flash) {
        this.flash = flash;
    }

    public String getBluetooth() {
        return bluetooth;
    }

    public void setBluetooth(String bluetooth) {
        this.bluetooth = bluetooth;
    }

    public String getImpressaoDigital() {
        return impressaoDigital;
    }

    public void setImpressaoDigital(String impressaoDigital) {
        this.impressaoDigital = impressaoDigital;
    }

    public String getInfraVermelho() {
        return infraVermelho;
    }

    public void setInfraVermelho(String infraVermelho) {
        this.infraVermelho = infraVermelho;
    }

    public String getMemoriaExpansivel() {
        return memoriaExpansivel;
    }

    public void setMemoriaExpansivel(String memoriaExpansivel) {
        this.memoriaExpansivel = memoriaExpansivel;
    }

    public String getSensores() {
        return sensores;
    }

    public void setSensores(String sensores) {
        this.sensores = sensores;
    }
}
