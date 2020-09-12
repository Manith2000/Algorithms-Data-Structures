#Quick Sort Algorithm (Implemented Recursively)
def quicksort(arr,start,end):
    if start < end:
        i = start #pointer1 initialises. this is the last no. before pivot
        for j in range(start,end):
            if arr[j] < arr[end]:  #if less than pivot at the end              
                arr[j],arr[i] = arr[i],arr[j] #swap the number and the last previous no. before pivot
                i += 1 #iterate by one since now our number is closer to pivot by one
        arr[i],arr[end] = arr[end],arr[i]
        quicksort(arr,start,i-1)
        quicksort(arr,i+1,end)

a = [4,1,6,2,7,2]
quicksort(a,0,len(a)-1)
print(a)