# Find the longest common subseq between to int arrays.
import math

def LCS(A,B):
    n = len(A)
    m = len(B)
    #Base case i == 0 or j == 0 then lcs = 0 (first col an first row set to zero)
    lcs = [ [ 0 for _ in range(0,m+1) ] for _ in range(0,n+1) ]
    
    
    # Sentinels at 0 in Array A and B
    A.insert(0,-math.inf)
    B.insert(0,-math.inf)

    #Bottom-up memo
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i] == B[j]:
                # My OPTIMAL SOLUTION will include for sure both elements A[i] and A[j] 
                #  => Add 1 to prefix to LCS( a_1...a_i-1 , b_1...b_j-1 ) 
                lcs[i][j] = lcs[i-1][j-1] + 1  
            else:
                # A[i] != A[j] my optimal solution will possibly include either A[i] or A[j]
                #  => Hence I need to guess if including A[i] or including A[j] would lead to an optimal.
                #     So LCS( A[1...i] , B[1...j-1] ) => If A[i] is by some chance in B[1..j-1] .
                #     So LCS( A[1...i-1] , B[1...j]) => If B[j] is by some chance in A[1...i]
                lcs_subproblem_with_Ai = -math.inf
                lcs_subproblem_wiht_Bj = -math.inf
                lcs_subproblem_with_Ai = lcs[i][j-1]
                lcs_subproblem_wiht_Bj = lcs[i-1][j]
                lcs[i][j] = max( lcs_subproblem_with_Ai , lcs_subproblem_wiht_Bj )

    return lcs[n][m]

def runTests():
    if LCS( [2] , [2] ) == 1 : 
        print("Test 1: Passed") 
    else: 
        print("Test 1: Failed") 
    
    if LCS( [3,1] , [2,3] ) == 1 : 
        print("Test 2: Passed") 
    else: 
        print("Test 2: Failed")
    
    if LCS( [2,3] , [3,1] ) == 1 : 
        print("Test 3: Passed") 
    else: 
        print("Test 3: Failed")

if __name__ == "__main__":
    with open("5_4_lcs.in") as f:
        next(f)
        A = list(  map(int, next(f).split(" ")) )
        next(f)
        B = list(  map(int, next(f).split(" ")) )
    
    runTests()
    
    print( LCS(A,B) )