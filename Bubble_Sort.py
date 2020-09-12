#Bubble Sort Algorithm
def bubblesort(arr): #ascending order
    a = np.asarray(arr) #converting list to array makes operations less tedious.
    # if a was list instead of array, need another for loop to iterate through unsorted list to check
    while any(a[1:]-a[:-1]<0): #any returns True for if any in array
        for i in range(1,len(a)): 
            if a[i-1] > a[i]: #if algorithm needs descending simply change this inequality
                a[i-1],a[i] = a[i], a[i-1]
    return a
arr = [2,3,1,5,2,6,2,5,2,7,1,402,24]
print(bubblesort(arr))