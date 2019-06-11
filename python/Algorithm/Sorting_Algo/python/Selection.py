import time

def selectionSort(array):
	start_time= time.time()	
	count=len(array) - 1	
	while(count >= 0):		
		largest = findLargestIndex(array,count)
		if (largest != count):
			swap(array,largest,count)
			
		count = count - 1
	exe_time = time.time() - start_time
	print("Execution time for Bubble sort = %5f" % (exe_time) )
		
def swap (array,index1,index2):
	temp=array[index2]
	array[index2]=array[index1]
	array[index1]=temp

def findLargestIndex(array,upperLimit):

	largestIndex=0
	
	for j in range (0, upperLimit +1 ):
		if (array[largestIndex] <= array[j]):
			largestIndex = j
	return largestIndex
	
	

arr1 = [200000,33 ,5,22,21,54,34,65456,65,654,35, 22,43,24,85,2 ];
arr2 = [9,8,7,6,5,4,3,2,1];
arr3 = [1,2,3,4,5,6,7,8,9];
arr4 = [];

print("Previous arrays:-")
print(arr1)
print(arr2)
print(arr3)
print(arr4)

selectionSort(arr1)
selectionSort(arr2)
selectionSort(arr3)
selectionSort(arr4)

print("After sorted arrays:-")
print(arr1)
print(arr2)
print(arr3)
print(arr4)



