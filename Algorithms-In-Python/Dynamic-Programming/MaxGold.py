import math

def maxGold(wg,N,W):
    dpTable = [ [ 0 for _ in range(N+1) ] for _ in range(W+1) ]
    for w in range(1,W+1):
        for i in range(1,N+1):
            dpTable[w][i] = dpTable[w][i-1]  # We need to first assume 
            if wg[i] <= w:
                x = dpTable[ w - wg[i] ][i-1] + wg[i]
                y = dpTable[w][i-1]
                dpTable[w][i] = max( x , y )
    return dpTable


if __name__ == "__main__":
    with open("6_1_knapsack.in") as f:
        W,N = map( int , next(f).split() )
        wg = list( map(int, next(f).split() ))
    #W = 10
    #N = 3           # number of gold lingots
    #wg = [1,4,8]     # w is the weight of each one.
    print( len(wg) )
    wg.insert(0,-math.inf)
    dpTable = maxGold(wg,N,W)
    print( dpTable[W][N] )