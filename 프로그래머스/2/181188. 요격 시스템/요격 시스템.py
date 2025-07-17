def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x:x[1])
    
    curr = 0
    
    for s,e in targets:
        if s >= curr:
            curr = e
            answer += 1
    
    return answer