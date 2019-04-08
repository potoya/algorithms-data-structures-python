#
# Input: n => number of objects  , [v1....vn] are the values per object. 
#        1 <= n <= 20 and 1 <= vi <= 30
#
# Output: 1 => if [v1...vn] can be partitioned into 3 parts with equal sum.
#         0 => Otherwise
#
# Mistakes in my Approach: I lost the logic of the subproblem and failed to
#                          understand that I needed more dimensions to remember more.
#                          Didn't see the application of knapsack because I tried to look
#                          at the Part-3 instead of thinking in Part-2 and Part-1 which
#                          would leave me to the subproblems.
import math

def partition3Memo(v,i,a,b,c, memo):
    key = str(i)+","+str(a)+","+str(b)+","+str(c) 
    print(key)
    if key in memo:
        print(1)
        return memo[key]
    
    if a == b and b==c:
        return True
    
    if i < 0:
        return False

    A = False
    if a - v[i] >= 0: 
        A = partition3Memo(v,i-1, a-v[i], b,c,memo)
    
    B = False
    if b-v[i]>= 0:
        B = partition3Memo(v,i-1,a, b-v[i],c,memo)
    
    C = False
    if c-v[i]>=0:
        C = partition3Memo(v,i-1,a,b,c-v[i],memo)
    
    q =  A or B or C
    memo[key] = q
    return q

#########################################
# Driver code
#########################################
if __name__ == "__main__":
    v = list(map(int,input().split(" "))) 
    S = sum(v)
    if S % 3 == 0:
        sum = S//3
        memo = {}  
        print( partition3Memo( v , len(v) - 1 , sum,sum,sum, memo) )
    else:
        len(v)
        print("?")
        print(False)