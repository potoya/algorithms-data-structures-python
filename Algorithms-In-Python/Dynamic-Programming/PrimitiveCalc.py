import math

#
# For n = 5
# 
# o1 => (+1) , o2 => (*2) , o3 => (+*3)
#
#  look for x in here => [inf inf inf inf inf inf] 
#                        [inf inf inf  1 0]     
#  
#
def minNumberOperationsNaive(n,x,memo):
    if memo[x] != math.inf:
        return memo[x]
    if n == x:
        return 0
    else:
        o1 = 1 + minNumberOperationsNaive(n ,x+1,memo) 
        o2 = 1 + minNumberOperationsNaive(n ,x*2,memo) if x*2 <= n else math.inf
        o3 = 1 + minNumberOperationsNaive(n ,x*3,memo) if x*3 <= n else math.inf
        q = min( o1 , o2 , o3 )
        memo[x] = q
        return q

#
#
#
def minNumOpsDp(n):
    minOperations = [ math.inf ] * (n+1)
    minOperations[n] = 0
    # loop from n back down to 1 calculating each time and storing answer in minOperations
    # We wil vary number "x" from n+1 downto 1
    for i in reversed(range(1,n)):
        # Min number of operations for adding 1.
        o1 = 1 + minOperations[i+1]
        
        # Min number of operations for mult by 2.
        o2 = math.inf
        if 2*i <= n:
            o2 = 1 + minOperations[2*i]
        
        # Min number of operations for mult by 3.
        o3 = math.inf
        if 3*i <= n:
            o3 = 1 + minOperations[3*i]
        
        # Take the minimum between all of them.
        q = min( o1 , o2 , o3 )
        
        # Record it in array so it can be accesible later.
        minOperations[i] = q
    
    return minOperations[1]

########################################################################################
# Main
########################################################################################
if __name__ == "__main__":
    n = 98734
    print( minNumOpsDp(n) )