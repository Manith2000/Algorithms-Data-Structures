#Quick Find is an algorithm to solve the dynamic connectivity problem

import numpy as np

#import integer array from text file into A
arr = open("array.txt","r+")
a = arr.readlines()
arr.close()
A= []
for i in a:
    A += [int(i.strip())]
print(A)

#assign id to each array element
id  = np.ndarray((len(A)))
for i in A:
    id[i] = i

#make function to check if two elements are connected
def connected(p,q):
    if id[p] == id[q]:
        return True
    else:
        return False

#make function to connect elements
def union(p,q):
    #change all elements with id of p to id of q
    idp = id[p] #make sure to state these before loop
    idq = id[q] #since id[p] changes.
    for i in id:
        if i == idp:
            i = idq
