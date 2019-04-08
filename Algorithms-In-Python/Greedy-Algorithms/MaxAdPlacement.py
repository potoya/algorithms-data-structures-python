###############################################################
# Problem Description
###############################################################
# 
# Input: First line contains integer n (number of slots for ads),
#        Second Line contains a1...an
#        Third line contains b1....bn
#
# Constraints: 1 <= n <= 10^3 , ai,bi = [-10^5,10^5] for all i from 1 to n
#
# Output: Max Sum( ai, ci ) where c1...cn in {1,..,bn} x {1,..,bn}
#

###############################################################
# Functions
###############################################################
def maxAdRevenue(n,a,b,):
    a.sort(reverse=True)
    b.sort(reverse=True)
    maxAdRevenue = 0
    for i in range(0,n):
        maxAdRevenue+=a[i]*b[i]
    return maxAdRevenue


###############################################################
# Main
###############################################################
if __name__ == '__main__':
    n = int( input() )
    a = list( map( int , input().split() ) )
    b = list( map( int , input().split() ) )
    print( maxAdRevenue(n,a,b) )