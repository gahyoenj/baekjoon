import math

def solution(n, k):
    answer = []
    person = [i for i in range(1,n+1)]
    
    k -= 1
    
    for i in range(n,0,-1):
        f = math.factorial(i-1)
        idx = k // f
        
        num = person.pop(idx)
        answer.append(num)
        
        k %= f
        
    
    return answer