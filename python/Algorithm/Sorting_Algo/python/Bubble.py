import time
import random

def BubbleSort (array ): 
	start_time= time.time()
	swapped=True
	size=len(array)
	
	for i in range (0,size):
		swapped=False
		
		for j in range (0,size-i-1):
			if (array[j] > array[j+1]):
				swap(array,j,j+1)
				swapped=True
				
		if(not(swapped)):
			break	
	exe_time = time.time() - start_time
	print("Execution time for Bubble sort = %5f" % (exe_time) )
	
def swap (array,index1,index2):
	temp=array[index2]
	array[index2]=array[index1]
	array[index1]=temp


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
			


def selectionSort(array):
	start_time= time.time()	
	count=len(array) - 1	
	while(count >= 0):		
		largest = findLargestIndex(array,count)
		if (largest != count):
			swap(array,largest,count)
			
		count = count - 1
	exe_time = time.time() - start_time
	print("Execution time for Selection sort = %5f" % (exe_time) )
		
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
	
print ("Random elements sort , array of elements ")
########################################################
arrBubRan=arr1
arrInsRan=arr1 
arrSelRan=arr1

print("Previous array:-")
print (arr1)

BubbleSort (arrBubRan)
selectionSort(arrSelRan)
insertionSort(arrInsRan)
print (" After the sorted ayyay (Bubble sort) = ", arrBubRan)
print (" After the sorted ayyay (Selection sort) = ", arrBubRan)
print (" After the sorted ayyay (Insertion sort) = ", arrBubRan)

print("\n \n \n")

print (" array of 10 elements worst case")
########################################################
arrBubRan=arr2
arrInsRan=arr2 
arrSelRan=arr2

print("Previous array:-")
print (arr2)

BubbleSort (arrBubRan)
selectionSort(arrSelRan)
insertionSort(arrInsRan)
print (" After the sorted ayyay (Bubble sort) = ", arrBubRan)
print (" After the sorted ayyay (Selection sort) = ", arrBubRan)
print (" After the sorted ayyay (Insertion sort) = ", arrBubRan)

print("\n \n \n")

print (" array of 10 elements best case ")
########################################################
arrBubRan=arr3
arrInsRan=arr3 
arrSelRan=arr3

print("Previous array:-")
print (arr3)

BubbleSort (arrBubRan)
selectionSort(arrSelRan)
insertionSort(arrInsRan)
print (" After the sorted ayyay (Bubble sort) = ", arrBubRan)
print (" After the sorted ayyay (Selection sort) = ", arrBubRan)
print (" After the sorted ayyay (Insertion sort) = ", arrBubRan)

print("\n \n \n")

print ("array of 0 elements ")
########################################################
arrBubRan=arr4
arrInsRan=arr4 
arrSelRan=arr4

print("Previous array:-")
print (arr4)

BubbleSort (arrBubRan)
selectionSort(arrSelRan)
insertionSort(arrInsRan)
print (" After the sorted ayyay (Bubble sort) = ", arrBubRan)
print (" After the sorted ayyay (Selection sort) = ", arrBubRan)
print (" After the sorted ayyay (Insertion sort) = ", arrBubRan)

print("\n \n \n")	
	
print ("Random elements sort , array of 1000 elements ")
########################################################
arrBubRan=[int(1000*random.random()) for i in range(1000)]
arrInsRan=arrBubRan 
arrSelRan=arrBubRan

BubbleSort (arrBubRan)
selectionSort(arrSelRan)
insertionSort(arrInsRan)
#print (" After the sorted ayyay (Bubble sort) = ", arrBubRan)
#print (" After the sorted ayyay (Selection sort) = ", arrBubRan)
#print (" After the sorted ayyay (Insertion sort) = ", arrBubRan)

print("\n \n \n")


print ("Random elements sort , array of 5000 elements ")
########################################################
arrBubRan=[int(5000*random.random()) for i in range(5000)]
arrInsRan=arrBubRan 
arrSelRan=arrBubRan

BubbleSort (arrBubRan)
selectionSort(arrSelRan)
insertionSort(arrInsRan)
#print (" After the sorted ayyay (Bubble sort) = ", arrBubRan)
#print (" After the sorted ayyay (Selection sort) = ", arrBubRan)
#print (" After the sorted ayyay (Insertion sort) = ", arrBubRan)

print("\n \n \n")

print ("Random elements sort , array of 10000 elements ")
########################################################
arrBubRan=[int(10000*random.random()) for i in range(10000)]
arrInsRan=arrBubRan 
arrSelRan=arrBubRan

BubbleSort (arrBubRan)
selectionSort(arrSelRan)
insertionSort(arrInsRan)
#print (" After the sorted ayyay (Bubble sort) = ", arrBubRan)
#print (" After the sorted ayyay (Selection sort) = ", arrBubRan)
#print (" After the sorted ayyay (Insertion sort) = ", arrBubRan)

print("\n \n \n")


print ("array of 5000 sorted elements as the best case ")
########################################################
listSorted = []
for _ in range (0,5000) :
	listSorted.append(_)

arrBubRan= listSorted
arrInsRan= listSorted
arrSelRan= listSorted

BubbleSort (arrBubRan)
selectionSort(arrSelRan)
insertionSort(arrInsRan)
#print (" After the sorted ayyay (Bubble sort) = ", arrBubRan)
#print (" After the sorted ayyay (Selection sort) = ", arrBubRan)
#print (" After the sorted ayyay (Insertion sort) = ", arrBubRan)

print("\n \n \n")


print (" array of 5000 reverced-sorted elements as the worst case ")
########################################################
listSorted = []
for k in range (0,5000) :
	listSorted.append(5000 - k)

arrBubRan= listSorted
arrInsRan= listSorted
arrSelRan= listSorted

#print(arrBubRan)

BubbleSort (arrBubRan)
selectionSort(arrSelRan)
insertionSort(arrInsRan)
#print (" After the sorted ayyay (Bubble sort) = ", arrBubRan)
#print (" After the sorted ayyay (Selection sort) = ", arrBubRan)
#print (" After the sorted ayyay (Insertion sort) = ", arrBubRan)

print("\n \n \n")
