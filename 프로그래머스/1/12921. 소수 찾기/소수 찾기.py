def solution(n):
    answer = 0
    is_prime = [True] * (n+1)
    is_prime[1] = False
    
    for i in range(2,int(n**0.5)+1):
        if not is_prime:
            continue
        for j in range(2*i,n+1,i):
            is_prime[j] = False
    answer = is_prime.count(True) -1
    
    return answer