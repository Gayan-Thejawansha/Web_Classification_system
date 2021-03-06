import time
import random

def selectPivot(arr,start,end):
	a= random.randint(start, end)
	b= random.randint(start, end)
	c= random.randint(start, end)
	if (arr[a] <= arr[b] <= arr[c] or arr[c] <= arr[b] <= arr[a]):
		return b
	elif (arr[b] <= arr[a] <= arr[c] or arr[c] <= arr[a] <= arr[b]):
		return a
	else:
		return c
	



def swap(array, index1,index2):
	temp = array[index2]
	array[index2] = array[index1]
	array[index1] = temp



def quickSort(array):
	less = []
	great = []
	equal = []
	if (len(array) <= 1):
		return array

	else: 
		pivotLoc=selectPivot(array,0,len(array)-1)
		pivot = array[pivotLoc]
				
		for element in array:

			if ( element > pivot):
				great.append(element)
			elif (element == pivot):
				equal.append(element)
			else:
				less.append(element)
		return quickSort(less) + equal + quickSort(great) 

array=[958,8,70,6,50,4,30,247,1,0,32,80,456,300,789,70,32,7889,7889,4789,5,7889]
print ("Before Sort:",array,". \n")
start_time=time.time()       
print("After sort by QuickSort=" ,quickSort(array))
print ("Execution time = ",(time.time()-start_time))
print("############################### \n \n \n")
