
import random

def selectPivot(array,start,end):
	one= random.randint(start, end)
	two= random.randint(start, end)
	thr= random.randint(start, end)
	middle= middleValue(array,one,two,thr)
	return middle
	
def middleValue(arr, a, b, c):
	if arr[a] <= arr[b] <= arr[c] or arr[c] <= arr[b] <= arr[a]:
		return b
	elif arr[b] <= arr[a] <= arr[c] or arr[c] <= arr[a] <= arr[b]:
		return a
	else:
		return c

def swap(array, index1,index2):
	temp = array[index2]
	array[index2] = array[index1]
	array[index1] = temp



def quickSort(array):

	if (len(array) <= 1):
		return array

	if (len(array)>1 ): 
		pivotLoc=selectPivot(array,0,len(array)-1)
		pivot = array[pivotLoc]
		i=0
		j=len(array)-1
		count = 0
		while((i < len(array) ) and ( j >= 0)):
			print (pivot) 
			print (array)	
			if ((array[i] >= pivot) and (array[j] < pivot) ):
				swap (array, i ,j)
			if(count%2 == 0):
				i = i + 1
			if (count%2 == 1):
				j = j - 1
			count = count + 1
			
		return quickSort(array[:j]) + quickSort(array[i:])

array=[9,8,7,6,5,4,3,2,1,0]       
print(quickSort(array))
