package aplicacao;

import entidades.*;
public class Testar {
    public static void main(String[] args) {
    
    Cliente cliente = new Cliente("João");
    ContaCorrente contacorrente = new ContaCorrente("João", 1500);
    ContaEspecial contaespecial = new ContaEspecial("João", 1500, 12000);



    contaespecial.dados();

    contaespecial.sacar(13000);

    contaespecial.dados();



    }

    
}
