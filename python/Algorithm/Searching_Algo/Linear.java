
import java.util.*;

public class Linear {

	
	public static void main(String [] args){
	
		Scanner sc = new Scanner(System.in);	

		//System.out.println(sc.nextInt());
	
		int arr [] = {33, 22,43,24,85,2 };
	
		System.out.println(linearSearch (arr , sc.nextInt()));
	
	}

	public static int linearSearch (int[] array, int key){
	
		for ( int i=0; i< array.length ; i++){
	
			if (array[i] == key) return i;
	
		}
		return -1;
	
	}




}
