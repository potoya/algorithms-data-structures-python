import math

def lcs3(a,b,c):
    n = len(a)
    m = len(b)
    o = len(c)
    lcsTable = [ [[0 for _ in range(0,o+1)] for _ in range(0,m+1) ] for _ in range(0,n+1) ]

    a.insert(0,-math.inf)
    b.insert(0,-math.inf)
    c.insert(0,-math.inf)
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            for k in range(1,o+1):
                if a[i] == b[j] and b[j] == c[k]:
                    lcsTable[i][j][k] = lcsTable[i-1][j-1][k-1] + 1
                else:
                    a = lcsTable[i][j-1][k-1]
                    b = lcsTable[i][j][k-1]
                    c = lcsTable[i][j-1][k]
                    d = lcsTable[i-1][j][k-1]
                    e = lcsTable[i-1][j][k]
                    f = lcsTable[i-1][j-1][k]
                    lcsTable[i][j][k] = max( a, b, c, d , e, b, f , c , e )       
    return lcsTable[n][m][o]

if __name__ == "__main__":
    with open("5_5_lcs3.in") as f:
        next(f)
        A = list(  map(int, next(f).split(" ")) )
        next(f)
        B = list(  map(int, next(f).split(" ")) )
        next(f)
        C = list(  map(int, next(f).split(" ")) )
    print( lcs3(A,B,C) )