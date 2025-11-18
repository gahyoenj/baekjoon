def solution(a):
    answer = 0

    left = [False] * len(a)
    right = [False] * len(a)
    minV = 2e10
    for i in range(len(a)):
        if a[i] <= minV:
            minV = a[i]
            left[i] = True
            continue
    
    minV = 2e10
    for i in range(len(a)-1,-1,-1):
        if a[i] <= minV:
            minV = a[i]
            right[i] = True
            continue
    
    for i in range(len(a)):
        if left[i] or right[i]:
            answer += 1
    return answer