package Dispositivos;

public class DispositivoCombinado extends Dispositivo implements Scanner, Impressora {

    public DispositivoCombinado(String numeroSerial) {
        super(numeroSerial);
    }

    @Override
    public void documentoProcessado(String documento) {
        System.out.println("Dispositivo Combinado processando: " + documento);
    }

    @Override
    public String scan() {
        return "Conteudo escaneado";
    }

    @Override
    public void print(String documento) {
        System.out.println("Conteudo imprimido: "+ documento);
    }

}
