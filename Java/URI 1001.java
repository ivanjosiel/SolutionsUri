 
import java.io.IOException;
 
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int a = entrada.nextInt();
        int b = entrada.nextInt();

        int soma = a + b;

        System.out.println("X = "+ soma);

        entrada.close();
    }
}
