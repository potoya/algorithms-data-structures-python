#
# Task: Given n points on a plane find the two points (xi,yi) and (xj,yj) with the min distance among them.
# Input: First l contains n number of points. Next n ls contain the points (xi,yi)
# Constraints: 2 < n <= 10^5 ; -10e9 <= xi,yi <= 10e9 are integers
# Output: Minimum distance with an accepted error of 10e-3 (4 digit precision at least)
# NOTE: There Can be two points that are the same point and hence the min distance will and can be 0.
import math

#############################################################################################################################
# Code
#############################################################################################################################

# Finds min distance by checking all pairs
def bruteForce(P):
    print("call: bruteforce( P=",len(P),")")
    dprime = distance(P[0],P[1])
    p1min = P[0]
    p2min = P[1]
    for i in range(0,len(P)):
        for j in range(1,len(P)):
            pi = P[i]
            pj = P[j]
            if distance(pi,pj) < dprime and i < j:
                dprime = distance(pi,pj)
                p1min = pi
                p2min = pj
    ret = (p1min,p2min,dprime)
    print("return: bruteforce(",ret,")")
    return ret

# Calculates distance
def distance(p1,p2):
    return pow(pow(p1[0]-p2[0] ,2) + pow(p1[1]-p2[1] ,2 ) , 0.5)

# Split Sorted arrays
def unMerge(Y,X_L):
    print("call: unmerge( ",len(Y) ,"," , len(X_L))
    n = len(Y)
    Y_L = []
    Y_R = []
    for i in range(0,n):
        print( i , n)
        if Y[i] in X_L:
            Y_L.append(Y[i])
        else:
            Y_R.append(Y[i])

    print("return: unmerge =>",len(Y_L),", ",len(Y_R))
    return (Y_L,Y_R)

# Gets closest pair within the strip (l-d,l+d)
def closestPairInStrip(Yprime):
    dprime = distance(Yprime[0],Yprime[1])
    p1prime = Yprime[0]
    p2prime = Yprime[1]
    #
    n = len(Yprime)
    for i in range(0,n):
        for j in range(1,n):
            pi = Yprime[i]
            pj = Yprime[j]
            if (pj[1] - pi[1]) < dprime:
                break
            elif distance(pi,pj) < dprime:
                dprime = distance(pi,pj)
                p1prime = pi
                p2prime = pj
    return (p1prime,p2prime,dprime)

# Gets the closest pair using divide and conquer
def closestPair(X,Y):
    print("call: closestPair(X = ",X, "Y = ",Y)
    if len(X) <= 3:
        return bruteForce(X)
    else:
        #Divide
        midIndex = math.ceil(len(X)/2)
        X_L = X[0:midIndex]
        X_R = X[midIndex:len(X)]
        midpoint = X[midIndex]
        #Conquer
        (Y_L,Y_R) = unMerge(Y,X_L)

        (cpp11,cp12, d1) = closestPair(X_L,Y_L)
        (cp21,cp22, d2) = closestPair(X_R,Y_R)
        
        d = min(d1,d2)

        #Combine
        Yprime = []
        for point in Y:
            (xi,yi) = point
            if xi-midpoint[0] < d:
                Yprime.append(point)

        ( p1min, p2min, dprime  ) = closestPairInStrip(Yprime)

        if dprime < d:
            return ( p1min, p2min, dprime  )
        else:
            if d == d1:
                return (cpp11,cp12, d1)
            else:
                return (cp21,cp22,d2)

#############################################################################################################################
# Input Data
#############################################################################################################################
if __name__ == "__main__":
    path = "4_6.in"
    with open(path) as f:
        n = int( next(f) )
        Y = []
        for i in range(1,n+1):
            xi,yi = map(int, next(f).split() )
            Y.append((xi,yi))
    Y.sort(key=lambda p: p[1])
    X = Y.copy()
    X.sort(key=lambda p:p[0])
    print( closestPair(X,Y) )