#Binary Search Algorithm - Iterative
def binarysearch(item,arr):
    #note that arr is an ascending sorted array
    start= 0
    end = len(arr) -1
    mid = round((start+end)/2)
    while start <=end: 
        mid = round((start+end)/2)
        if item == arr[mid]:
            return "The item %s was found at index %s" %(item,mid) #stops the while loop
        elif item > arr[mid]:
            start = mid + 1 #ignore the lower half of array
        elif item < arr[mid]:
            end = mid - 1 #ignore upper half of array
    return "The item %s was not found" %(item)


#Binary Search- Recursive
def binaryrecursive(item,arr):
    if len(arr) < 2:
        if arr[0] != item:
            return 'The item %s was not found' %(item)
        else:
            return 'The item %s was found' %(item)
    else:
        start= 0
        end = len(arr) - 1
        mid = round((start+end)/2)
        if item == arr[mid]:
            return "The item %s was found" %(item) 
        elif item > arr[mid]:
            start = mid + 1 #ignore the lower half of array
            print(arr[start:])
            return binaryrecursive(item,arr[start:])
        elif item < arr[mid]:
            end = mid - 1 #ignore upper half of array
            print(arr[:end])
            return binaryrecursive(item,arr[:end])

A = [1,2,2,2,3,4,5,5]
print(binaryrecursive(2,A))