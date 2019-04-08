'''
A = a1...an : ai are Ints for all 1 <= i <= n
k is int , k > 0
Minimize ( max{ Sum( p1 , p2 , ..., pk  } )

k = 2  A = [ 1 2 3 6 ] => SUBPROBLEM: k = 2  A = [1 2 3]  ai = 6
'''
import math

# Bottom-up dp implementation - O(k*N^2)
# a - array of numbers
# n - subproblem form n....1
# k - kth partition
def optPartDp(a,n,k):
    dp =[ [ 0  for _ in range(n+1) ] for _ in range(k+1) ]
    
    a.insert(0, math.inf)
    
    # k == 1
    for i in range(1,n+1):
        dp[1][i] = sum( a[1:i+1] )
    
    # n == 1
    for i in range(1,k+1):
        dp[i][1] = a[1]

    for i in range(2,k+1):
        for j in range(2,n+1):
            best = math.inf
            for p in range(1,j+1):
                best = min( best , max( dp[i-1][p] , sum( a[p+1:j+1] ) ) )
            dp[i][j] = best

    return (dp[k][n], dp)

# Naive recursive implementation
# a - array of numbers
# n - subproblem form n....1
# k - kth partition
def optPartRec(a,n,k):
    if n == 1:
        return a[0]
    elif k == 1:
        return sum( a[0:n] )
    else:
        optimum = math.inf
        for j in range(1,n):
            o1 = optPartRec(a,j,k-1)
            o2 = sum( a[j:n] )
            optimum = min(optimum, max(o1, o2))
        return optimum

####################################################
# Driver Code
####################################################
if __name__ == "__main__":
    a = [100,200,300,400,500,600,700,800,900]
    k = 3
    n = len(a)
    test = optPartDp(a,n,k)
    print(test)