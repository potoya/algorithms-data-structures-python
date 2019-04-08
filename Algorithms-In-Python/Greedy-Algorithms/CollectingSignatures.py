#
# Input: First line contains number of 'n' line segments. Next 'n' lines contain (ai, bi)
# Constraints: n = [1,100], 0<=ai<=bi<=10^9 for all i = [0,n]
# Output: 2 lines. First should contain number of minimum m points, second line should show n coordinates for each point.
#
def minPointsContainedBySegments(x,n):
    m=[]
    x.sort(key = lambda t: t[0] )
    i = 0
    while i < n:
        bi = x[i][1]
        d = 1
        for j in range(i+1,n):
            segment = x[j]
            aj=segment[0]
            bj=segment[1]
            if bi >= aj:
                d+=1
            if bi > bj:
                bi = bj
        i+=d
        m.append(bi)
    return m

# prints the output from the array m recieved.
def printOutput(m):
    print(len(m))
    for x in m:
        print(x, end=' ')

if __name__ == '__main__':
    n = int(input())
    x = []
    for i in range(0,n):
        ai,bi = map(int, input().split())
        x.append( (ai,bi) )
    m = minPointsContainedBySegments(x,n)
    printOutput(m)