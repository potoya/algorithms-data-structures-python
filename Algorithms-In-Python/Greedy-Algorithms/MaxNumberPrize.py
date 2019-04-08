#################################################################
# Problem Description
#################################################################

#Input Format.
# The input consists of a single integer n .Constraints.1≤n≤109.
# Output Format.
# In the first line, output the maximum number푘such that푛can be represented as a sumof푘pairwise distinct positive integers. 
# In the second line, output푘pairwise distinct positive integersthat sum up to푛(if there are many such representations,
#  output any of them).
# Sample 1.
# Input:6
# Output:
# 6
# 1 2 3

#################################################################
# Functions
#################################################################
import math

def maxNumbersPrize(n):
    arr = []
    i = 1
    sum = 0
    while i <  math.ceil( (n-sum)/2 ) :
        arr.append(i)
        sum +=i
        i+=1
    arr.append(n-sum)
    return arr

#################################################################
# Main
#################################################################
if __name__ == '__main__':
    n = int(input())
    l = maxNumbersPrize(n)
    print( len(l) )

