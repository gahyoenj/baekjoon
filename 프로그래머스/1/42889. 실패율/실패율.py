def solution(N, stages):
    answer = []
    cnt = [[i,0,0] for i in range(1,N+1)]
    
    print(cnt)
    
    for stop in stages:
        
        if stop != N+1:
            cnt[stop-1][2] += 1
        
        for finish in range(stop-1):
            cnt[finish][1] += 1
    
    
    rate = [[i,0] for i in range(1,N+1)]
    
    for idx, clear, fail in cnt:
        if clear + fail != 0:
            rate[idx-1][1] = fail / (clear+fail)
    
    rate.sort(key=lambda x:(-x[1],x[0]))
    
    for i,r in rate:
        answer.append(i)
    
    return answer