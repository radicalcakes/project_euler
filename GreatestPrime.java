//port my solution to java
import java.util.Scanner;

public class GreatestPrime {
    public static int greatestPrime(int n){
        if(n == 0){
	    return 0;
	}
	else if(n == 1){
	    return 1;
	}
	else{

	int i = 2;

	while(i <= Math.pow(n,0.5)){
	    if(n % i == 0){
                n /= i;
	    } else {
	        i++;
	    }
	}
	 return n;
	}
    }

    public static void main(String[] args){
	Scanner in = new Scanner(System.in);

	System.out.println("Enter an int to be factored: ");
	int v = in.nextInt();

	System.out.printf("Greatest prime factorization: %d", v);
	System.out.println("");
    }


}
