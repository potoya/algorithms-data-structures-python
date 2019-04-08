import math
#--------------------------------------------------------------------
# Functions
#--------------------------------------------------------------------

def DpChange( money , coins ):
    minNumCoins = [math.inf]*(money+1)
    minNumCoins[0] = 0
    for m in range(1,money+1):
        for i in range( 0 , len(coins) ):
            if m >= coins[i]:
                    minNumCoins[m] = min( minNumCoins[m] , minNumCoins[ m - coins[i] ] + 1 )
    return ( minNumCoins[money] , minNumCoins )

#--------------------------------------------------------------------
# Main
#--------------------------------------------------------------------

if __name__ == "__main__":
    money = 950
    coins = [1,3,4]
    print( DpChange(money,coins) )
