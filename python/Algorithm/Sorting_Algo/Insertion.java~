
public class Insertion {

	public static void main( String [] args) {
	
		//int arr [] = {33 ,5,22,54,65456,65,654,35, 22,43,24,85,2 };
		//int arr [] = {9,8,7,6,5,4,3,2,1};
		//int arr [] = {1,2,3,4,5,6,7,8,9};
		int arr []= {5};
		insertionSort(arr);
		for(int var: arr)
		System.out.print(var + " ");
		System.out.println();
	}

	public static void insertionSort(int [] array){
	
		int j,temp;
		
		for(int i=1; i < array.length ; i++){
			temp=array[i];
			j=i-1;
			

			//System.out.println("j="+ j +" "+ "temp=" +temp + " _and_ array,j="+array[j]);			
			while ( temp < array[j] ) {
				//System.out.println(array[j] +" to "+array[j+1]);
				array[j+1]=array[j];
				j--;
				if(j==0) break;
				
			}
	//			System.out.println(temp +" _to_ "+array[j+1]);			
			array[j+1]=temp;
		}	
	
	}

}
