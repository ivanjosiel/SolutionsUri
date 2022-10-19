import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner i = new Scanner(System.in);
		int a = i.nextInt();
		int total = a;
		int ano = a/365;
		a -=(ano*365);
		int mes = a/30;
		a -= (mes*30);
		int dia =a;
		System.out.printf("%d ano(s)\n", ano);
		System.out.printf("%d mes(es)\n", mes);
		System.out.printf("%d dia(s)\n", dia);
		
		
	}
}
