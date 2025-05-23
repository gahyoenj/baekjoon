def solution(n, stations, w):
    answer = 0
    cov = 2*w+1
    prev = 0
    
    for c in stations:
        end = c - w -1
        gap = end - prev
        
        if gap > 0:
            answer += (gap+cov-1) // cov
        
        prev = c + w
    
    if prev < n:
        answer += (n-prev+cov-1) // cov
    
    return answer