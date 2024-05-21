package aplicacao;

import entidades.Mamifero;
import entidades.Peixe;

public class TestarAnimais {
    public static void main(String[] args) {

        Mamifero camelo = new Mamifero("Camelo", 150, 4, "Amarelo", "Terra", 2.0, "Vegetais");
        Peixe tubarao = new Peixe("Tubarão", 300, 0, "Cinzento", "Mar", 1.5, "Barbatanas e caudas");
        Mamifero ursocanada = new Mamifero("Urso-do-Canadá", 180, 4, "Vermelho", "Terra", 0.5, "Mel");
    
        camelo.dadosMamifero();
        tubarao.dadosPeixe();
        ursocanada.dadosMamifero();
    }
}
