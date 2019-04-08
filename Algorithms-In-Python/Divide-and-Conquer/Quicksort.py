#QuickSort algorithm
from random import randint

def getRandIndex(l,r):
    return randint(l,r)

def swapElements(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partStage(A,l,r,callback):
    # Start first partition stage.
    x = A[l]
    j = l   # Will separate A into [l...j] <= x and [j+1...r] > x
    for i in range(l+1,r+1):
        if callback(i,j,x):
            swapElements(A,j+1,i)
            j+=1
    return j
    
    
def partition3(A,l,r):
    # Randomize pivot selection
    randomPivotIndex = getRandIndex(l,r)
    #print(randomPivotIndex)
    swapElements(A,l,randomPivotIndex)
    
    # Start first partition stage.
    # x = A[l]
    # j = l   # Will separate A into [l...j] <= x and [j+1...r] > x
    # for i in range(l+1,r+1):
    #     if A[i] <= x and i != j:
    #         swapElements(A,j+1,i)
    #         j+=1

    # m2 = j
    
    m2 = partStage(A,l,r, lambda i,j,x :  A[i] <= x and i != j )

    # Place all elements =x trailing to the pivot at m2.
    v = l
    for u in range(l+1,r+1):
        if A[u] == x:
            swapElements(A,v+1,u)
            v+=1
    
    equalToX = A[l:v+1]
    n1 = v+1-l

    lessThanX = A[v+1:m2+1]
    n2 = (m2+1)-(v+1)
    
    A[l:l+n2] = lessThanX
    A[l+n2:l+n2+n1] = equalToX
    
    m1 = l+n2
    return (m1,m2)

def quickSort(A,l,r):
    if l>=r:
        return
    else:
        (m1,m2) = partition(A,l,r)
        quickSort(A,l,m1-1)
        quickSort(A,m2+1,r)