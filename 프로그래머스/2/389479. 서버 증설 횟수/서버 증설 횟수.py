def solution(players, m, k):
    answer = 0
    server = [0] * 24
    
    for i, n in enumerate(players):
        
        if i-k >=0 and server[i-k] > 0:
            server[i-k] = 0
        
        if n // m >= 1 and n // m > sum(server[:i]):
            server[i] = n // m - sum(server[:i])
            answer += server[i]
    return answer