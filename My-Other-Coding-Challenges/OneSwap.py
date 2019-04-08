'''
Input: Unsorted array a[1]...a[n]
Output: 1 if a[1]..a[n] has #inversions = 1.    
        0 if #inversions = 0
        1 if #inversions = -1
'''

import math

# Challenge Implementation  
def isSorted(a):
    return all( a[i] < a[i+1] for i in range(len(a)-1))

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def oneSwap(a):
    n = len(a)
    i = 0
    j = n-1

    #Check ascending order disruptor.
    k1 = 0
    i+=1
    while i < j:
        if a[i] < a[i-1]:
            k1 = i-1
            break
        i+=1

    #Check descending ord disruptor.
    k2 = 0
    j-=1
    while j > k1:
        if a[j] > a[j+1]:
            k2 = j+1 
            break
        j-=1

    swap(a,k1,k2)
    return isSorted(a)



######################################
# Driver Code
######################################
if __name__ == "__main__":
    a = [1,8,4,5,7,2,9]
    test = oneSwap(a)
    print(test)