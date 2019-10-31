import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner i = new Scanner(System.in);
		int a = i.nextInt();
		int total = a;
	    int cem = a/100;
	    a -= (cem*100);
	    int cinquenta = a/50;
	    a -= (cinquenta*50);
		int vinte = a/20;
	    a -= (vinte*20);
	    int dez = a/10;
	    a -= (dez*10);
	    int cinco = a/5;
	    a -= (cinco*5);
	    int dois = a/2;
	    a -= (dois*2);
	    int um = a/1;
	    a -= (um*1);
	    System.out.printf("%d\n",total);
	    System.out.printf("%d nota(s) de R$ 100,00\n",cem);
	    System.out.printf("%d nota(s) de R$ 50,00\n",cinquenta);
	    System.out.printf("%d nota(s) de R$ 20,00\n",vinte);
	    System.out.printf("%d nota(s) de R$ 10,00\n",dez);
	    System.out.printf("%d nota(s) de R$ 5,00\n",cinco);
	    System.out.printf("%d nota(s) de R$ 2,00\n",dois);
	    System.out.printf("%d nota(s) de R$ 1,00\n",um);
   }
}
