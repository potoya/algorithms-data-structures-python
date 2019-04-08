###########################
# Minimum distance problem
# O(n) using a map
###########################
import math

def solution(a):
    dictionary = {}
    for i in range(len(a)):
        num = a[i]
        if num in dictionary:
            match = dictionary[num]

            last_matching_index = match[0]
            min_dist = match[1]

            new_min_dist = min(i - last_matching_index, min_dist)
            if new_min_dist != min_dist:
                dictionary[num] = (i, new_min_dist)
        else:
            # Add new num to map
            dictionary[num] = (i, math.inf)

    b = []
    for num in dictionary:
        b.append( dictionary[num][1] )

    return min(b)

##########################
# Driver Code
##########################
if __name__ == '__main__':
    a = [7, 1, 7, 7, 1, 7]
    print(solution(a))
