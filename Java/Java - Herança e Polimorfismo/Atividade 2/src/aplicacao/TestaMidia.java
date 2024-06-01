package aplicacao;

import java.util.Scanner;
import java.util.Random;

public class TestaMidia {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        Midia[] lista = new Midia[10];

        Random aleatorio = new Random();

        int aleat, codigo, nData;   
        double preco;
        String nome;
        int opcao;

        
        preco = 30*aleatorio.nextDouble() + 20;

        for (int i=0, contc=0, contd=0; i < 2; i++) {
            aleat = aleatorio.nextInt(2);

            if (0==aleat) {
                System.out.println("Criando um CD!");

                preco = 15*aleatorio.nextDouble() + 15;

                nome = "CD" + contc;

                nData = aleatorio.nextInt(15) + 5;

                lista[i] = new Cd(contc, preco, nome, nData);
                contc++;
            }
            else {
                System.out.println("Criando um DVD!");

                preco = 30 * aleatorio.nextDouble() + 20;

                nome = "DVD" + contd;

                nData = aleatorio.nextInt(15) + 20;

                lista[i] = new Dvd(contd, preco, nome, nData);

                contd++;


            }
        }

        for (int i = 0; i < 2; i++) {
            lista[i].printDados();
        }


        
        

    }
}