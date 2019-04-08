# Uses python3

#####################################################
# Classes
#####################################################

class FixedStack:
    def __init__(self,n):
        self.maxSize=n
        self.list = []
    
    def push(self,element):
        if len(self.list) == self.maxSize:
            self.list.pop(0)
        self.list.append(element)
    
    def toString(self):
        s = ''
        for i in range(0,len(self.list)):
            s += str( self.list[i] )
        return s

#####################################################
# Functions
#####################################################


#
# Computes the pisano count for Fib n mod m
# m >= 2
#
def pisanoPeriod(m, fibModList):
    # period for m>=2
    previous = 0
    current  = 1
    count = 2 # var to count length of m.
    
    fixedStack = FixedStack(3)
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

# Compute fib last digit sum
# input n = [0,10e18]
def fibLastDigitSum(n):
    if n == 0:
        return 0
    
    x = calcFibMod(n+2,10)
    if x == 0 : 
        x += 10
    return x-1

# Compute fib last digit partial sum 
# Input: Integer m,n 
# Output: (Fm+Fm+1+...+Fn) mod 10
# Constraints: 0 <= m <= n <= 10e18
#
def fibLastDigitPartialSum(m,n):
    if m == 0:
        return fibLastDigitSum(n)
    u = fibLastDigitSum(n)
    v = fibLastDigitSum(m-1)
    if u < v:
        u += 10
    return u - v

    

#####################################################
# Main
#####################################################

if __name__ == '__main__':
    from_,to = map( int , input().split() )
    print( fibLastDigitPartialSum(from_,to) )
