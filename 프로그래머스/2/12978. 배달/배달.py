def solution(N, road, K):
    answer = 1
    village = [[] for _ in range(N+1)]
    for v1,v2,time in road:
        village[v1].append((v2,time))
        village[v2].append((v1,time))
        
    # print(village)
    
    dist = [2e10] * (N+1)
    dist[1] = 0
    
    q = [(1,0)]
    
    while q:
        node,t = q.pop(0)
        
        if dist[node] < t:
            continue
        
        for after, time in village[node]:
            newT = time + t
            
            if newT < dist[after]:
                dist[after] = newT
                q.append((after,newT))
    
    for i in range(2,N+1):
        if dist[i] <= K:
            answer += 1
    
    return answer