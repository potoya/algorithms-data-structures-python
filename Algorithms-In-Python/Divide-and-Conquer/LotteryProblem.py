import math
import collections
import numpy

#
# Solution using sort and binary search for range scan. O(n*log n)
#

def binarySearch(A,target,rangeType):
    low = 0
    high = len(A)-1
    while low <= high:
        mid = math.ceil( (high+low)/2 )
        if target == A[mid]:
            if rangeType == "EXCLUSIVE":
                return mid+1
            else:
                return mid
        elif target < A[mid]:
            high = mid-1
        else:
            low = mid+1
    return low

def lotteryCount(A,S,C):
    A.sort()
    i = 0
    for x in S:
        ai = x[0]
        bi = x[1]
        ra = binarySearch(A,ai,"INCLUSIVE")
        rb = binarySearch(A,bi,"EXCLUSIVE")
        C[i] = rb-ra
        i+=1

if __name__ == "__main__":
    S = []
    A = []
    with open("4_5_lottery.in","r") as f:
        # Reads line 0
        n,t = map(int,next(f).split())
        # Reads lines 1 to n inclusive
        for i in range(1,n+1):
            ai,bi = map(int, next(f).split() )
            print(i,ai,bi)
            S.append( (ai,bi) )
        # Reads a one line array of numbers into A at line n+1
        A = list( map(int, next(f).split() ) )
        C = [0]*n
        lotteryCount(A,S,C)
        print(sum(C))
    