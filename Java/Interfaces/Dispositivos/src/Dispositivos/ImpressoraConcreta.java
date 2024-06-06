package Dispositivos;

public class ImpressoraConcreta extends Dispositivo implements Impressora{

    public ImpressoraConcreta(String numeroSerial) {
        super(numeroSerial);
    }

    @Override
    public void documentoProcessado(String documento) {
        System.out.println("Impressora processando: "+ documento);

    }

    @Override
    public void print(String documento) {
        System.out.println("Conteudo imprimido: "+ documento);
    }
    
}
