#Two pointer searching algorithm

#Variants: Opposite & Equi directional


#Two Sum Problem: two numbers add up to target
def twosum(arr,target):
    #this can be solved using opposite directional
    #note that the array arr is sorted
    pointerone = 0
    pointertwo = len(arr)-1
      #initialise
    while pointerone < pointertwo:
        targettemp = (arr[pointerone] + arr[pointertwo])
        if targettemp > target:
            pointertwo -= 1
        elif targettemp < target:
            pointerone += 1
        else:
            return 'Numbers ' + str(arr[pointerone]) + ' & ' + str(arr[pointertwo]) + ' at indexes: ' + str(pointerone) + ' & ' + str(pointertwo)
    return 'Not Found' #returns if doesnt find target sum

arr = [-3,2,3,3,6,8,15]
print(twosum(arr,10))


#Max sum of subarray
#Also solved this using sliding window method (see Algorithms github folder)


def maxsum(arr,x): #subarray size x
    