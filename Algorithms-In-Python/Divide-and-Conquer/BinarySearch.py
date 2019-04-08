#
# Remember to implement binary search of translation problem in C++ using pointers. (Watch binary search video.)
#
import math

def binarySearch(A,low,high,key):
    mid = low + (high-low)//2
    if key == A[mid] or low >= high:
        return mid
    elif key > A[mid]:
        return binarySearch(A,mid+1,high,key)
    elif key < A[mid]:
        return binarySearch(A,low,mid-1,key)

def binarySearch2(A,low,high,key):
    target = -1
    while low <= high:
        mid = low + (high-low)//2
        if key == A[mid]:
            target = mid
            break
        elif key < A[mid]:
            high = mid-1
        else:
            low=mid+1
    return (target,A[target])

def binarySearch3(A,low,high,key):
    while low <= high:
        mid = math.ceil( (high+low)/2 )
        print(low,high,mid)
        if key == A[mid]:
            return (True,mid,A[mid])
        elif key < A[mid]:
            high = mid-1
        else:
            low = mid+1
    return (False,low,high)

if __name__ == '__main__':
    A=[9,3,-2,8,10,20,15]
    A.sort()
    print( A, binarySearch3(A,0,len(A)-1,4) )
    # a = list( map(int, input().split()) )

    # b = list( map(int, input().split()) )
    # res = 0
    # arr = []
    # for i in range(len(b)):
    #     t = binarySearch2(a,0,len(a)-1,b[i]) 
    #     arr.append(t)
    #     if t == -1 : 
    #         res+=1
    # print(" ")
    # print(res)
    # print(arr)
    # print(len(arr))