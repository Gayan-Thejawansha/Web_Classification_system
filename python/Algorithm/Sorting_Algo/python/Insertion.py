import time

def insertionSort(array):
	start_time= time.time()	
	for i in range (1, len(array)):
		temp = array[i]
		j = i - 1
		while ( temp < array[j]):
			#print(array)
			array[j+1] = array[j]
			j=j-1
			if ( j== -1):
				break
		
		array [j+1] =temp
	exe_time = time.time() - start_time
	print("Execution time for Insertion sort = %5f" % (exe_time) )	
			


arr1 = [200000,33 ,5,22,21,54,34,65456,65,654,35, 22,43,24,85,2 ];
arr2 = [9,8,7,6,5,4,3,2,1];
arr3 = [1,2,3,4,5,6,7,8,9];
arr4 = [];

print("Previous arrays:-")
print(arr1)
print(arr2)
print(arr3)
print(arr4)

insertionSort(arr1)
insertionSort(arr2)
insertionSort(arr3)
insertionSort(arr4)

print("After sorted arrays:-")
print(arr1)
print(arr2)
print(arr3)
print(arr4)
			
