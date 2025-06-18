def solution(x, y, n):
    answer = 0
    result = []
    q = [(y,0)]
    find = False
    
    while q:
        now, cnt = q.pop(0)
        answer = cnt + 1
        
        if now == x:
            find = True
            answer = cnt
            break
        
        elif now > 0:
            if now % 3 == 0:
                q.append((now//3,answer))
            if now % 2 == 0:
                q.append((now//2,answer))
            
            q.append((now-n,answer))
            
    if not find:
        answer = -1
    return answer