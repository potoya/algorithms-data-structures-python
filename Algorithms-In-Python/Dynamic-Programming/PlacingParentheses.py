'''
Input: d[1] + op[1] + d[2] + op[2] + ........ op[n-1] + d[n]
Output: Max value possible of the arithmetic expressions choosing order of operations.

Debuging Tip: Reduce input size and check errors. Then grow input size.
'''
import math


def maxOrderOfOperations(d, op):
    n = len(d)
    m = [[0 for i in range(0, n)] for j in range(0, n)]
    M = [[0 for i in range(0, n)] for j in range(0, n)]

    for i in range(0, n):
        m[i][i] = d[i]
        M[i][i] = d[i]

    # Subproblems are equal to the amount of operators.
    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            (a, b) = minAndMax(m, M, i, j)
            m[i][j] = a
            M[i][j] = b

    return M[0][n-1]


'''
Calculates de min and max table checking all the possibilities for a given subproblem.
'''


def minAndMax(m, M, i, j):
    minimum = math.inf
    maximum = -math.inf
    for k in range(i, j):
        a = calc(M[i][k], M[k+1][j], op[k])
        b = calc(M[i][k], m[k+1][j], op[k])
        c = calc(m[i][k], M[k+1][j], op[k])
        d = calc(m[i][k], m[k+1][j], op[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return (minimum, maximum)


'''
Helper function to operate two operands with an operator.
'''
def calc(d1, d2, op):
    if op == '-':
        return d1-d2
    elif op == "*":
        return d1*d2
    elif op == "+":
        return d1+d2


###############################################
# Driver Code
###############################################
if __name__ == "__main__":
    inputList = list("7+6+3-2-7-4*2+4+2-9*6*8")
    d = [int(inputList[i]) for i in range(0, len(inputList)) if i % 2 == 0]
    op = [inputList[i] for i in range(0, len(inputList)) if i % 2 == 1]
    print(maxOrderOfOperations(d, op))
