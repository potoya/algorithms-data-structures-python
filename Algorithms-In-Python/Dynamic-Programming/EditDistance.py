########################################################################################
# Edit distance using dynamic programming
########################################################################################
import math

# 
# Task: Get the optimal solution (Alignment problem string)
#
def backtrack(i,j):
    #TODO: Implementation
    return "Pending"

def editDistance(A,B):
    n = len(A)
    m = len(B)
    D =[ [ 0 for j in range(0,m+1) ] for i in range(0,n + 1) ] # Matrix of zeros n*m.
    
    for i in range(0,n+1):
        D[i][0] = i

    for j in range(0,m+1):
        D[0][j] = j
    
    A.insert(0,"#") # Inserted sentinel
    B.insert(0,"#") # Inserted sentinel

    for i in range(1,n+1):
        for j in range(1,m+1):
            # Case where we choose to do an insertion in A[i]. This means that A[j] value is chosen 
            # so we need to ask for the subproblem editDistance(A[i],A[j-1]).
            # A[1....i]  -
            # A[1..j-1] A[j]
            insertions = D[i][j-1] + 1

            # This case is analogous to the other one, with the difference that here we choose A[i]
            # and delete A[j] so our subproblem would be editDistance(A[i-1],A[j]).  
            # A[1..i-1] A[i]
            # A[1....j]  -
            deletions = D[i-1][j] + 1
            matchOrMisMatch = D[i-1][j-1]
            if A[i] != B[j]:
                # A[1..i-1] A[i]
                # A[1..j-1] A[j]
                matchOrMisMatch += 1
            D[i][j] = min( insertions, deletions , matchOrMisMatch )
    
    return D[n][m]





########################################################################################

if __name__ == "__main__":

    with open("5_3_edit_distance.in") as f:
        strA = next(f)
        strB = next(f)

    A = list(strA)
    #A = []
    B = list(strB)
    #B = []
    print(editDistance( A , B ) )    
