#Linear Search Algorithm
def linearsearch(item,arr):
    #note this finds every instance of the item within array
    for i in range(0,len(arr)):
        if item == arr[i]:
            return "The element %s was found at index %s" %(arr[i],i)