import java.util.Scanner;

public class App {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int[] vet = new int[10];
        int i = 0;
        int x, r, cont = 0;

        // Leitura dos valores do vetor
        System.out.println("Digite 10 valores para o vetor: ");

        for (; i < 10; i++) {

            vet[i] = sc.nextInt();
        }

        //Visualizaçao de números pares
        System.out.println("Será exibido apenas os valores pares: ");

        for (int j = 0; j < 10; j++) {
            r = vet[j]%2;

            if (r==0) {
                cont++;
            }
        }
        System.out.println("A quantidade de valores pares é" + cont);

        sc.close();
    }
}