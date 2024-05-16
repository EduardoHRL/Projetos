package aplicacao;

import entidades.Empregado;
import entidades.Gerente;
import entidades.Vendedor;

public class Testar {
    public static void main(String[] args) {

        Empregado empregado = new Empregado("João", 1000);
        Gerente gerente = new Gerente("Ariel", 5000, "Produção");
        Vendedor vendedor = new Vendedor("Eduardo", 1500, 25);

        empregado.dados();
        gerente.dados();
        vendedor.dados();

    }
}
