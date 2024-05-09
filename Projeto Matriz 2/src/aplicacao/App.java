
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.printf("Digite a quantidade de linhas da matriz: ");
        int linhas = sc.nextInt();

        System.out.printf("Digite a quantidade de colunas da matriz: ");
        int colunas = sc.nextInt();

        int[][] mat = new int[linhas][colunas];

        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                System.out.printf("Digite o valor da posição da Linha %d e Coluna %d", linhas, colunas);
                mat[i][j] = sc.nextInt();
            }
        }

        System.out.printf("Digite um valor que pertence a matriz: ");
        int valor = sc.nextInt();

        System.out.printf("\nValores a esquerda, direita, a cima e a baixo do valor\n");

        for (int i = 0; i < mat.length; i++) {

        }
    }

}
