# Taskey: Checkey if an input sequence has a majority key (count > n/2)
# Input: a0,a1,...,an of non-neg integers
# [1,2,1,3,1,1]
# [1,1,1] [3,1,2] #check if Right side has a (n/2+1 - LeftMajorCount)
# Design using divide and conquer to find majority element in n*logn
# Study how to do it in O(n)
#
import math
import operator
class Candidate:
    def __init__(self,id,count):
        self.id = id
        self.count = count

def checkCandidateMajority(c,a,n):
        v = a.count(c.id) # counts in T(n)=n/2
        c.count += v
        if c.id != None and c.count >  n/2:
            return True
        else:
            return False
        
def combineMajority(leftCandidate,rightCandidate,L,R):
    n = len(L)+len(R)
    if checkCandidateMajority(rightCandidate,L,n):
        return rightCandidate
    elif checkCandidateMajority(leftCandidate,R,n):
        return leftCandidate
    else:
        return Candidate(None,0)

def majorityElement(a):
    n = len(a)
    if n == 1:
        return Candidate(a[0],1)
    else:
        q = math.ceil(n/2)
        L = a[0:q]
        R = a[q:n]
        leftCandidate = majorityElement(L)
        rightCandidate = majorityElement(R)
        return combineMajority(leftCandidate,rightCandidate,L,R)

if __name__=='__main__':
    n = int( input() )
    s = open("4_2_majority_element.in","r").read()
    #s = input()
    a = list( map(int, s.split() ) ) 
    element = majorityElement(a)
    if element.id != None:
        print(1)
        print(element.id, element.count)
    else:
        print(0)

    correctMajority(a)

    