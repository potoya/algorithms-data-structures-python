#find the number of inversions in an array. (How many numbers are in bad order)
# Example:
#   [1,2,3,4,5,6] => numInv = 0
#   [6,5,4,3,2,1] => numInv = 5 + 4 + 3 + 2 + 1 = 5(6)/2 = 15

#   [2,3,9,2,9] => numInv = 2
#   DIV & CONQ => merge( [2,3], [2,9,9])
#                 1. [2,] 

import math

def mergeNumInv(L,R):
    numInv = 0
    output = []
    n1 = len(L)
    n2 = len(R)
    i = 0
    j = 0
    for loop_count in range(0,n1+n2):
        if i == n1:
            output.append(R[j])
            j+=1
        elif j==n2:
            output.append(L[i])
            i+=1
        elif L[i] > R[j]:
            output.append(R[j])
            numInv += n1 - i
            j+=1
        else: #(L[i] <= R[j] )

            output.append(L[i])
            i+=1
    return (output,numInv)

def mergeSortNumInv(A):
    n = len(A)
    if n == 1:
        return ([A[0]],0)
    else:
        q = math.ceil(n/2)
        (L,numInvLeft) = mergeSortNumInv(A[0:q])
        (R,numInvRight) = mergeSortNumInv(A[q:n])
        (A_prime, numInvPrime) = mergeNumInv(L,R) 
        return (A_prime, numInvPrime + numInvLeft + numInvRight)

#############################################
# Input
#############################################
if __name__ == "__main__":
    with open("4_4_inversions.in","r") as f:
        n = int( next(f) )
        a = list(map(int, next(f).split() ))
    print( mergeSortNumInv(a) )