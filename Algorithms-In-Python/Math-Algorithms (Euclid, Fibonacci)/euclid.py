import sys

def euclid(a,b):
    if b==0:
        return a
    else:
        return euclid(b,a%b)

if __name__ == "__main__":
    numbers = input().split()
    a, b = map(int, numbers)
    print( euclid(a,b) )