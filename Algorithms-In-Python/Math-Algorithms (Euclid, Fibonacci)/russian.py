def rec_russsian(a,b):
    if a == 0 : 
        return 0
    if a % 2 == 0 :
        return 2*rec_russsian(a/2,b)
    return b+2*rec_russsian((a-1)/2,b)
    
print(rec_russsian(40,7))


