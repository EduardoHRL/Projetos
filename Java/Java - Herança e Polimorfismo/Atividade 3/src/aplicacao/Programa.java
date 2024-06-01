package aplicacao;

import java.util.Scanner;
import java.util.Random;
import entidades.*;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Arquivo[] vet = new Arquivo[4];

        Random aleatorio = new Random();

        int aleat, tamanho, downloads, visualizacoes;
        String nome;
        double preco;

        for (int i = 0, mp3 = 0, mp4 = 0; i < 4; i++) {
            aleat = aleatorio.nextInt(2);

            if (0 == aleat) {
                System.out.println("Criando um mp3!");

                nome = "Mp3 " + mp3;

                preco = aleatorio.nextInt(100) + 50;

                tamanho = aleatorio.nextInt(10240) + 1024;

                downloads = aleatorio.nextInt(1000000);

                vet[i] = new Mp3(nome, preco, tamanho, downloads);
                mp3++;

            } else {
                System.out.println("Criando um mp4!");

                nome = "Mp4 " + mp4;

                preco = aleatorio.nextInt(2500) + 100;

                tamanho = aleatorio.nextInt(25000) + 50000;

                visualizacoes = aleatorio.nextInt(1000000);

                if (visualizacoes > 10000) {
                    preco += 0.08;
                }

                vet[i] = new Mp4(nome, preco, tamanho, visualizacoes);
                mp4++;
            }
        }
        System.out.printf("\nAntes do reajuste\n");
        for (int i = 0; i < 4; i++) {

            vet[i].printDados();
        }

        for (Arquivo produto : vet) {
            if (produto instanceof Mp3) {
                ((Mp3) produto).reajuste();
            } else if (produto instanceof Mp4) {
                ((Mp4) produto).reajuste();
            }
        }

        System.out.printf("\n\nDepois do reajuste\n");
        
        for (int i = 0; i < 4; i++) {

            vet[i].printDados();
        }
    }
}
