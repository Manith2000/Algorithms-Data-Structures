# Selection Sort Algorithm
def selectsort(arr):
    sorted = []
    for i in range(len(arr)): #iterate through unsorted part
        sorted += [min(arr)]  
        arr.remove(min(arr))   
    return sorted
arr = [4,5,1,6,2,2,5,5,3,3,6]
print(selectsort(arr))