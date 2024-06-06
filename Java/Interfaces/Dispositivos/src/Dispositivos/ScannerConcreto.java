package Dispositivos;

public class ScannerConcreto extends Dispositivo implements Scanner{

    public ScannerConcreto(String numeroSerial) {
        super(numeroSerial);
    }

    @Override
    public void documentoProcessado(String documento) {
        System.out.println("Scanner processando: " + documento);
    }

    @Override
    public String scan() {
        return "Conteudo escaneado";
    }
    
}
