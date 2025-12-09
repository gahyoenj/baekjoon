def solution(n):
    answer = 0
    if n == 0:
        return 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer