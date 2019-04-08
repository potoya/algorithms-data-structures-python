# Uses python3
def calc_fib(n,m):
    f=[0,1]
    count = 2
    for i in range(2,n+1):
        f.append( f[i-1]+f[i-2] )
        
    return f[n]



print(calc_fib(n))
