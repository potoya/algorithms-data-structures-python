# Input format. 
# The first line of the input contains the number n of compounds and the capacity W of a backpack. 
# The next n lines define the prices and weights of the compounds. The i-th line contains the
# price per pound pi and the weight wi of the i-th compound.
# 
# Output format. 
# Output the maximum price of compounds that fit into the backpack.
# 
# Constraints. 
# 1 ≤ n ≤ 103, 0 ≤ W ≤ 2 · 106; 0 ≤ pi ≤ 2 · 106, 0 < wi ≤ 2 · 106
# for all 1 ≤ i ≤ n. All the numbers are integers.

################
# Functions
################

def orderBy(tup):
    return tup[0]/tup[1]

def maxValueOfLoot( n , W , l ):
    # sort by vi/wi
    l.sort( key = orderBy , reverse = True) 
    # loop through sorted list -> take the most valuable, accumulate, eliminate from list.
    maxloot = 0.0 # max loot (double)
    r = W # remaining capacity
    for e in l:
        if r == 0:
            break
        vi = e[0]
        wi = e[1]
        if wi > r:
            maxloot += (vi/wi)*r
            r -= r
        else:
            maxloot += vi
            r -= wi
    return maxloot


###############
# Script
###############
if __name__ == '__main__':
    n,W = map( int, input().split() )
    l=[]
    for i in range(n):
        vi,wi = map(int, input().split())
        l.append( (vi,wi) )
    
    maxLoot = maxValueOfLoot(n,W,l)
    print( round(maxLoot,4) ) 