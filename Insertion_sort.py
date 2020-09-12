#Insertion Sort Algorithm
def insertionsort(arr):
    sort = [arr[0]]
    arr.remove(arr[0])
    for i in range(0,len(arr)):
        for j in range(0,len(sort)):
                if arr[i] <= sort[j]:
                    sort.insert(j,arr[i])
                    break
                elif arr[i] > max(sort):
                    sort.append(arr[i])
                    break
    return sort
arr = [34,2,53,6,3,51,24,6,3,6]
print(insertionsort(arr))