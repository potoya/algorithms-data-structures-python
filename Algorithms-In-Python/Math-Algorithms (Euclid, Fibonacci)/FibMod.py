import MyDataStructures

#
# Computes the pisano count for Fib n mod m
# m >= 2
#
def pisanoPeriod(m, fibModList):
    # period for m>=2
    previous = 0
    current  = 1
    count = 2 # var to count length of m.
    
    fixedStack = MyDataStructures.FixedStack(3)
    fixedStack.push(0)
    fixedStack.push(1)
    
    fibModList.append(0)
    fibModList.append(1)
    
    timesSeen011 = 0 # the loop will look for two ocurrences of 011
    while timesSeen011 < 2:
        previous, current = current, previous + current
        # calculate current modulus and put in stack
        mod = current % m
        fibModList.append(mod)
        fixedStack.push( mod ) 
        count += 1
        if fixedStack.toString() == '011':
            timesSeen011+=1

    period = count - 3
    return period

#
# Computes fib(n) mod m
# Input => 1 <= n <= 10e18 , 2 <= m < 10e5
# Output => fib(n) mod m
def calcFibMod(n,m):
    fibModList = []
    p = pisanoPeriod(m,fibModList) # Calculate pisano count for fib.
    index = n % p
    return fibModList[index]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(calcFibMod(n, m))