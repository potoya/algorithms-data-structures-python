#
# Input: A set of n tuples  [ (i,j) for i,j in range(n) ]  
# Output: Number with most frequent Id in all of the ranges.
#
import math
from itertools import chain

'''
Solution in O(MaxDomain):

Input - (1,5)(2,4)(8,9)(1,3)

Frequency Table
index   0   1   2   3   4   5   6   7   8   9   10    iter     Registered
freq    0  +1   0   0   0   0  -1   0   0   0   0      2        [(1,5)]
freq    0  +2  +1   0   0  -1  -2   0   0   0   0      3      [(1,5),(2,4)]
.
.
.
-------------------------------------------------------------------------------
freq <- will have the information of which numbers are included in the range
        with one pass.

Intuition tip: 
Note that if you do this trick for an input of just (1,5) how would you get the
information out? It's simple to see that you loop through an array and have the 
+1 signal that will add one from the start to the range onwards and then you turn
off that signal with the -1 to to the opposite.
'''
# Impl
def getLuckyId(a):
    maxDomain = getMaxFromTupleList(a)
    freq = [ 0 for _ in range(maxDomain+2) ]

    #Step 1: Count all the ranges.
    for (x1,x2) in a:
        freq[x1] += 1
        freq[x2+1] -= 1
    
    #Step 2: Prefix sum calculation
    for i in range(1,len(freq)):
        freq[i] = freq[i-1] + freq[i]
    
    luckyId = freq.index( max(freq) )
    return (freq, luckyId)  


# Help
def getMaxFromTupleList(a):
    aprime = list(chain.from_iterable(a))
    return max(aprime)


###########################################
# Driver Code
###########################################
if __name__ == "__main__":
    a = [(1,5),(2,4),(8,9),(1,3)]
    #a = [(1,5)]
    test = getLuckyId(a)
    print(test)