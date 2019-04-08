# Merge sort implementation.
import math
def merge(L,R):
    n1 = len(L)
    n2 = len(R)    
    i=0
    j=0
    output = []
    for loopCount in range(0,n1+n2):
        if j==n2:
            output.append(L[i])
            i+=1
        elif i==n1:
            output.append(R[j])
            j+=1
        elif L[i] <= R[j]:
            output.append(L[i])
            i+=1
        else: 
            #L[i] > R[j]:
            output.append(R[j])
            j+=1
    return output

# Count in a tuple array while keys remain sorted.
def mergeSort(a):
    n = len(a)
    if n == 1:
        return [a[0]]
    else:
        q = math.ceil(n/2)
        L = mergeSort( a[0:q] )
        R = mergeSort( a[q:n] )
        return merge(L,R)

#
# REMEMBER TO DO MERGE SORT AND COUNT FOR THE NUMBER OF INVERSION PROBLEM !
#