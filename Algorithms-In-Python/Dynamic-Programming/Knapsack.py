####################################
# Knapsack Problem
####################################
import math

def maxValueKnapsack( values , weights , W_capacity ):
    n = len(weights)  # number of elements
    maxValueTable = [ [ 0 for _ in range(n+1) ] for _ in range(W_capacity + 1) ]

    values.insert(0,-math.inf)
    weights.insert(0,-math.inf)
    for i in range(1,n+1):
        for w in range(1,W_capacity +1 ):
            if weights[i] <= w:
                maxValueTable[w][i] = max( maxValueTable[ w - weights[i] ][i-1] + values[i] , maxValueTable[w][i-1] )
            else:
                maxValueTable[w][i] = maxValueTable[w][i-1]
    return maxValueTable[W_capacity][n]
    


####################################

if __name__ == "__main__":
    v = [30,14,16,9]
    w = [6,3,4,2]
    print( maxValueKnapsack( v , w , 10) )