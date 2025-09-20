def solution(a, b, n):
    answer = 0
    
    while n //a > 0:
        bottle = (n // a) * b
        n = (n % a) + bottle
        answer += bottle
    
    return answer