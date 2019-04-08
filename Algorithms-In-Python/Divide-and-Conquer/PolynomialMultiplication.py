def naiveMulty(A,B,n):
    product = [0]*(2*n-1)
    for i in range(0,n):
        for j in range(0,n):
            product[i+j] += A[i]*B[j]
    return product

# FASTER WAY IS DONE USING KARATSUBA TO SPLIT POLYNOMIAL INTO D1*x^n/2 + D0*x^n/2

if __name__ == '__main__':
    A = [3,2,5]
    B = [5,1,2]
    print( naiveMulty(A,B,3) )