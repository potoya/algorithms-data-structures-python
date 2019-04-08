# Uses python3
import sys

def lcm(a,b):
    gcd = euclid(a,b)
    return (a*b)//gcd # Python can perform integer division (or floor division) with "//" operator.

def euclid(a,b):
    if b==0:
        return a
    else:
        return euclid(b,a%b)

if __name__ == "__main__":
    numbers = input().split()
    a, b = map(int, numbers)
    print( lcm(a,b) )
