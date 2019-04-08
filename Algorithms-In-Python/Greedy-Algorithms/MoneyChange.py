# Functions
############
def calcMinCoins(m):
    tot = 0
    coinValues = [10,5,1]
    r = m
    for coinVal in coinValues:
        q = r // coinVal
        if q > 0:
            tot += q
        r %= coinVal
    return tot
    

############
# Script
############
if __name__ == '__main__':
    m = int(input())
    print( calcMinCoins(m) )
