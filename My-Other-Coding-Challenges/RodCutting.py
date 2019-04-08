import math

# Two Options:
# 1 - I dont cut the rod and my revenue = p[n-1]
# 2 - I cut the rod in two pieces (i ,n-i) with revenue = p[i] + revenue(n-i) for all i between [0,n-2] 
# It can also be done by eliminating the comparison done with p[n-1] and letting i for all i in [0,n-1]
def maxRevRodCutting_TopDownMemo_Aux(p,n,r):
    if r[n-1] >= 0:
        return r[n-1]
    if n == 0:
        q = 0
    else:
        q = -math.inf
        for i in range(0,n-2):
            optimumLocal = max( p[n-1], p[i] + maxRevRodCutting_TopDownMemo_Aux(p, ((n-1)-i) ,r) )
            q = max(q, optimumLocal )
        r[n-1] = q
    return q


#Implementation of top-down memo.
def maxRevRodCutting_TopDownMemo(p,n):
    r = [-math.inf]*(n)
    return maxRevRodCutting_TopDownMemo_Aux(p,n,r)

#
# Bottom-up implementation
# Note: Differences in indexing.
#      ( 1 <= j <= n ) corresponds to the n elements after 0. (Subproblem domain)
#      ( 0 <= i <= j ) corresponds to the array domain.
# Key parts:
#     a) r[j-i-1] to search for subproblem
#     b) r[j] to update current problem
def maxRevRodCutting_BottomUpMemo(p,n):
    r = [-math.inf]*(n+1)
    r[0] = 0  # <- solution for subproblem of size j = 1 will be stored here.
    for j in range(1,n+1):
        q = -math.inf
        for i in range(0,j):
            q = max( q , p[i] + r[j-i-1] )
        r[j] = q
    return r[n]


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20]
    n = len(p)
    print( maxRevRodCutting_BottomUpMemo(p,n) )