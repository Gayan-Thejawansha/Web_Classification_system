
public class Selection {

	public static void main( String [] args) {
	
		int arr [] = {200000,33 ,5,22,21,54,34,65456,65,654,35, 22,43,24,85,2 };
		//int arr [] = {9,8,7,6,5,4,3,2,1};
		//int arr [] = {1,2,3,4,5,6,7,8,9};
		//int arr []= {};
		selectionSort(arr);
		for(int var: arr)
		System.out.print(var + " ");
		System.out.println();
	}
	
	
	public static void selectionSort(int array []){
	
		int largest;
		for(int i=array.length-1;i>=0 ;i--) {
			largest=findLargestIndex(array,i);
			if(largest !=i ) {
				swap(array,largest,i);
			}
		}
	}
	
	public static int findLargestIndex(int array [], int upperLimit ){
	
		int largestIndex=0;
		
		for(int j=0; j<=upperLimit;j++) {
			if(array[largestIndex]< array[j]) largestIndex=j;
		}	
		return largestIndex;
	}
	
	public static void swap(int [] array, int index1, int index2){
	
	int temp=array[index2];
	array[index2]=array[index1];
	array[index1]=temp;	
	}	

}
