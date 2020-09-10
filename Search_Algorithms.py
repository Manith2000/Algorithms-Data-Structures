#Linear Search Algorithm
def linearsearch(item,arr):
    #note this finds every instance of the item within array
    for i in range(0,len(arr)):
        if item == arr[i]:
            return "The element %s was found at index %s" %(arr[i],i)
    

#Binary Search Algorithm - Iterative
def binarysearch(item,arr):
    #note that arr is an ascending sorted array
    start= 0
    end = len(arr) -1
    mid = round((start+end)/2)
    while start <=end: 
        mid = round((start+end)/2)
        if item == arr[mid]:
            Found = True
            return "The item %s was found at index %s" %(item,mid) #stops the while loop
        elif item > arr[mid]:
            start = mid + 1 #ignore the lower half of array
        elif item < arr[mid]:
            end = mid - 1 #ignore upper half of array
    return "The item %s was not found" %(item)


#Binary Search- Recursive



#Comparing the time for both algorithms 
#Plotted the array size- run time
#Used the timeit module to measure runtime of program

import numpy as np
import timeit

size = []
time_lin = []
time_bin = []

for i in range(100,1000000,100):
    A = np.arange(0,i,1)
    size += [len(A)]
    time_lin += [timeit.timeit('''
import numpy as np
def linearsearch(item,arr):
    #note this finds every instance of the item within array
    for i in range(0,len(arr)):
        if item == arr[i]:
            return "The element %s was found at index %s" %(arr[i],i)
    print(linearsearch(53643,A))        
            ''',number = 500)/500]
    time_bin += [timeit.timeit('''
import numpy as np
def binarysearch(item,arr):
    #note that arr is an ascending sorted array
    start= 0
    end = len(arr) -1
    mid = round((start+end)/2)
    Found = False
    while start <=end:
        mid = round((start+end)/2)
        if item == arr[mid]:
            Found = True
            return "The item %s was found at index %s" %(item,mid)
        elif item > arr[mid]:
            start = mid + 1
        elif item < arr[mid]:
            end = mid - 1
    return "The item %s was not found" %(item)
    print(binarysearch(53643,A))        
            ''',number = 500)/500]
import matplotlib.pyplot as plt
plt.plot(np.asarray(size),np.asarray(time_lin))
plt.plot(np.asarray(size),np.asarray(time_bin))
plt.legend(["Linear Search", "Binary Search"])
plt.ylabel('Time (s)')
plt.xlabel('Input Size (array no. of elements)')
plt.show()