#Merge Sort Algorithm (Implemented Recursively)

def merge(A,L,R): #function sorts two lists L & R onto list A by merging
    i = 0
    j =0
    k = 0
    NL= len(L)
    NR = len(R)
    while (i < NL) and (j < NR):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1 
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while (i  < NL): #only one of the follow two while loops will run 
        A[k] = L[i]  #this ensure that if L or R has put all its items. the remaining items are sorted to A
        i += 1
        k += 1
    while (j< NR):
        A[k] = R[j]
        j += 1
        k += 1
    return A


def mergesort(arr):
    if len(arr) < 2:
        return arr #one number is already sorted
    else:
        n = round(len(arr)/2)
        L = []
        R = []    
        for item in arr[:n]: #add items to arr L & R, splitting the array
            L += [item]
        for item in arr[n:]:
            R += [item]
        mergesort(L) #sorts either side of whole array
        mergesort(R)
        return merge(arr,L,R) #merge the sorted two parts into one array
    
A = [4,2,5,2,5,2]
print(mergesort(A))