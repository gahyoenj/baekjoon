def next(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n+1) // 2
    
def solution(n,a,b):
    answer = 0
    if a > b:
        a,b = b,a
        
    while answer <= n//2:
        answer += 1
        
        if b-a == 1 and b % 2 == 0:
            break
        a = next(a)
        b = next(b)
        
    return answer