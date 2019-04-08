# Application of divide and conquer. Type "Google Interview in youtube"
# Done with binary search.
# Takeaway a lot of interaction and help given due to first implementing naive. 
# The key was realizing the trick of (any pi at left) < Actual < (any pi at Right)
# E.g find am wher m = 2
#     [10,2,5,3,11] -> after one inner loop -> [2,5,3,10,11] the spotIndex for 10 is found to be 3!
#     BUT since  any(2,5,3) < 10 < any(11) we find ourselves to possible sub problems.
#     In this case m = 2 < spotIndex = 3 soo you choose (2,5,3) and iterate again.
#     Avg Running time is => n (all are looped) + n/2 (Only half) + n/4 (half of half) + .. ~ 2n => O(n)
#     
# Can also be done in a Recursive fashion by setting up the inner loop first as the BASE case
# and partitioning recursively calling. (Should Implement this part later.) MINE DOES in place,
# the other would possibly require doing array copies using more memory.

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def partition(A,q):
    x = A[q]
    swap(A,q,0)
    n = len(A)
    j = 0
    for i in range(1,n):
        if A[i] <= x:
            swap(A,i,j+1)
            j+=1
    swap(A,0,j)
    return j

def findMthStatistic(a,m):
    # m is the target index.
    N = len(a)
    x1=0
    x2=N-1
    while x1 < x2:
        spotIndex = x1
        spotIndex = partition(A,spotIndex)
        # for i in range(x1+1,x2+1):
        #     if a[spotIndex] > a[i]:
        #         # single swap
        #         if spotIndex == i - 1: # implies a[spotIndex] > a[i] (next element) 
        #             swap(a,spotIndex,i)
        #             spotIndex = i
        #         else:
        #             #double swap (protect spotIndex?)
        #             swap(a,spotIndex,spotIndex+1)
        #             spotIndex = spotIndex+1
        #             swap(a, spotIndex-1, spotIndex+1)
        if m < spotIndex:
            x2 = spotIndex-1
        elif m > spotIndex:
            x1 = spotIndex+1
        else:
            # m == 0
            break     
    return a[x1]

# Try cases that might break spotIndex+1
A=[-40, -20, 10, 10]

print(findMthStatistic(A,2))


