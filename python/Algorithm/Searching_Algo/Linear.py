
import random
import os

'''
	public static int linearSearch (int[] array, int key){
	
		for ( int i=0; i< array.length ; i++){
	
			if (array[i] == key) return i;
	
		}
		return -1;
	
	}
'''

def linearSearch(array , key):
	
	for i in range (0,len(array)):
		if (array[i]==key):
			return i
	return -1
	

arr = [33, 22,43,24,85,2]
key=24
print (linearSearch(arr,key))
		
	
