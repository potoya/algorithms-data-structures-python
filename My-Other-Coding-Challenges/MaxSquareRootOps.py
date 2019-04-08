# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#Input: A and B integers.
#Ouput: Max number of square root ops for numbers in [A,B] interval.
#
# Example.
import math

def solution(A, B):
    best = -math.inf
    for number in range(A,B+1):
        num_sqrt_ops = 0
        acc = math.sqrt(number) 
        while acc % 1 == 0:
            num_sqrt_ops += 1
            acc = math.sqrt(acc)
        if num_sqrt_ops > best:
            best = num_sqrt_ops
    return best

if __name__ == "__main__":
    print(solution(6000,7000))