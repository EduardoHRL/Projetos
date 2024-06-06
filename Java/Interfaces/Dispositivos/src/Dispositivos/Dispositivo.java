package Dispositivos;

public abstract class Dispositivo {

    public String numeroSerial;

    public Dispositivo(String numeroSerial) {
        this.numeroSerial = numeroSerial;
    }

    public String getNumeroSerial() {
        return numeroSerial;
    }

    public void setNumeroSerial(String numeroSerial) {
        this.numeroSerial = numeroSerial;
    }

    public abstract void documentoProcessado(String documento);
    
}
