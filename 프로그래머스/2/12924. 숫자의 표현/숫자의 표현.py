def solution(n):
    answer = 0
    for i in range(1,n+1):
        sumV = 0
        current = i
        while sumV < n:
            sumV += current
            current += 1
        
        if sumV == n:
            answer += 1
    return answer