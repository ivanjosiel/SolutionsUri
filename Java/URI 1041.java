import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner i = new Scanner(System.in);
		String x = i.nextLine();
	    String[]a = x.split(" ");
	    double um = Double.parseDouble(a[0]);
	    double dois = Double.parseDouble(a[1]);
	    if(um != 0 || dois != 0) {
	  
	    if(um>0 && dois>0)
		   System.out.printf("Q1\n");
	    
		if(um<0 && dois>0)
		   System.out.printf("Q2\n");
		
		if(um<0 && dois<0)
		   System.out.printf("Q3\n");
		
		if(um>0 && dois<0)
		   System.out.printf("Q4\n");
		
		if(um==0 && dois!=0)
			System.out.printf("Eixo Y\n");		   	
		    if(um!= 0 && dois==0)
		    	System.out.printf("Eixo X\n");
	    }
	    else{
	 	
	    	System.out.printf("Origem\n");
	    	System.exit(0);
	    	
	 

}
	}
}
