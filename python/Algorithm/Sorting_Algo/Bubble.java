
import java.util.*;


public class Bubble {

	public static void main( String [] args) {
	
		//int arr [] = {33 ,5,22,54,65456,65,654,35, 22,43,24,85,2 };
		int arr [] = {9,8,7,6,5,4,3,2,1};
		bubbleSort(arr);
		for(int var: arr)
		System.out.print(var + " ");
		System.out.println();
	}

	public static void bubbleSort(int [] array){
		int compares=0, swaps=0;
		int sizeOfArray= array.length;
		boolean swapped=true;
		
		for(int i=0; i< sizeOfArray && swapped; i++) {
			swapped= false;
			
			for(int j=0; j< sizeOfArray-i-1; j++) {
			compares++;
			
				if( array[j] > array[j+1]){
					swaps++;
					swap(array,j,j+1);
					swapped=true;
				}			
			}		
		}
		System.out.println("Comparisons="+ compares);
		System.out.println("Swapes="+swaps);	
	}
	
	public static void swap(int [] array, int index1, int index2){
	
	int temp=array[index2];
	array[index2]=array[index1];
	array[index1]=temp;	
	}



}
