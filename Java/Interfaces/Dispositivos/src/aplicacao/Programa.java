package aplicacao;

import Dispositivos.ImpressoraConcreta;
import Dispositivos.ScannerConcreto;
import Dispositivos.DispositivoCombinado;

public class Programa {

	public static void main(String[] args) {

		ImpressoraConcreta p = new ImpressoraConcreta("1080");
		p.documentoProcessado("My Letter");
		p.print("My Letter");

		System.out.println();
		ScannerConcreto s = new ScannerConcreto("2003");
		s.documentoProcessado("My Email");
		System.out.println("Scan result: " + s.scan());
		
		System.out.println();
		DispositivoCombinado c = new DispositivoCombinado("2081");
		c.documentoProcessado("My dissertation");
		c.print("My dissertation");
		System.out.println("Scan result: " + c.scan());
	}
}