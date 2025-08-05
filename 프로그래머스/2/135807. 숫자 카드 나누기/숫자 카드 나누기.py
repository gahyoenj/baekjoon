import math

# def find(arr):
#     for num in range(arr[0],0,-1):
#         check = True
#         for a in arr[1:]:
#             if a % num != 0:
#                 check = False
#                 break
#         if check:
#             return num

def solution(arrayA, arrayB):
    answer = 0
    
#     arrayA.sort()
#     arrayB.sort()
    
#     gcdA = find(arrayA)
#     gcdB = find(arrayB)
    gcdA, gcdB = 0 , 0

    for i in range(len(arrayA)):
        gcdA = math.gcd(gcdA,arrayA[i])
    
    for i in range(len(arrayB)):
        gcdB = math.gcd(gcdB,arrayB[i])
    
    for idx in range(len(arrayA)):
        if arrayA[idx] % gcdB == 0:
            gcdB = 1
        
        if arrayB[idx] % gcdA == 0:
            gcdA = 1
    
    
    if gcdA == 1 and gcdB == 1:
        answer = 0
    
    else:
        answer = max(gcdA,gcdB)


    
    
    return answer