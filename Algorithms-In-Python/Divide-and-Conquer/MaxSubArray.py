import math

#Output: (x1,x2,maxSum) where A[x1...x2] is the subarray with maxSum
def maxSubArray(A,low,high):
    n = high - low + 1
    if  low >= high:
        return (low,high,A[low])
    else:
        mid = int((low+high)/2)
        L_MaxSubArr = maxSubArray(A,low,mid)
        R_MaxSubArr = maxSubArray(A,mid+1,high)
        M_MaxSubArr = maxCrossingSubarray(A,low,mid,high)
        if L_MaxSubArr[2] >= R_MaxSubArr[2] and L_MaxSubArr[2] >= M_MaxSubArr[2]:
            return L_MaxSubArr
        elif R_MaxSubArr[2] >= L_MaxSubArr[2] and R_MaxSubArr[2] >= M_MaxSubArr[2]:
            return R_MaxSubArr
        else:
            return M_MaxSubArr
        
def maxCrossingSubarray(A,low,mid,high):
    maxLeftSum = -9999999
    k1 = low
    sum = 0
    for i in reversed(range(low,mid+1)):
        sum+=A[i]
        if sum >= maxLeftSum:
            maxLeftSum = sum
            k1 = i
    
    maxRightSum = -9999999
    k2 = mid+1
    sum = 0
    for j in range(mid+1,high+1):
        sum+=A[j]
        if sum >= maxRightSum:
            maxRightSum = sum
            k2 = j
    return (k1,k2, maxLeftSum+maxRightSum)

# 
def maxSubArraySingleScan(A,low,high):
    sum = A[low]
    maxSum = A[low]
    x1 = 0
    x2 = 0
    for i in range(low+1,high+1):
        sum+=A[i]
        if sum-A[i] < 0 and A[i] > sum-A[i]:
            x1 = i
            x2 = i
            maxSum = A[i]
            sum = maxSum
        elif sum > 0 and sum > maxSum:
            x2 = i
            maxSum = sum  
    return (x1,x2,maxSum)

A = [29,-3,-25,28,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print("MaxSubArr O(n*logn)",maxSubArray(A,0,6)) 
print("MaxSubArr O(n)",maxSubArraySingleScan(A,0,6))