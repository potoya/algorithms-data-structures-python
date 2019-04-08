# Let isSubsetSum(arr, n, sum/2) be the function that returns true if 
# there is a subset of arr[0..n-1] with sum equal to sum/2
# The isSubsetSum problem can be divided into two subproblems
#  a) isSubsetSum() without considering last element 
#     (reducing n to n-1)
#  b) isSubsetSum considering the last element 
#     (reducing sum/2 by arr[n-1] and n to n-1)
# If any of the above the above subproblems return true, then return true. 
# isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) ||
#                               isSubsetSum (arr, n-1, sum/2 - arr[n-1])
#
#
#   ( Knapsack Application Problem )
#
import math

def partition2(arr,sum):
    if sum % 2 == 1: 
        return False

    n = len(arr)
    sumPossible = [ [ False for _ in range(sum+1) ] for _ in range(n+1) ] 
    
    for i in range(0,sum+1):
        sumPossible[0][i] = False

    for i in range(0,n+1):
        sumPossible[i][0] = True 

    arr.insert(0,-math.inf)

    for i in range(1,n+1):
        for s in range(1,sum+1):
            sumPossible[i][s] = sumPossible[i-1][s]
            if arr[i] <= s:
                sumPossible[i][s] = sumPossible[ i-1 ][ s-arr[i] ] or sumPossible[i-1][s]
    return sumPossible[n][sum//2]
       
#########################################
# Driver code
#########################################
if __name__ == "__main__":
    while(True):
        constant = int(input())
        arr = [1,5,3,3]
        arr = list( map( lambda x: x * constant, arr) )
        print( partition2( arr , sum(arr) ) )   