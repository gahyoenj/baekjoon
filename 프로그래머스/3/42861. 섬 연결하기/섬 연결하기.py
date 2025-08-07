import heapq

def solution(n, costs):
    answer = 0
    
    island = [[] for _ in range(n)]
    
    
    visited = [False] * n
    
    for i1,i2,cost in costs:
        island[i1].append((i2,cost))
        island[i2].append((i1,cost))
        
    heap = []
    
    visited[0] = True
    
    for go, c in island[0]:
        heapq.heappush(heap,(c,go))
    
    while heap:
        cost, to = heapq.heappop(heap)
        
        if not visited[to]:
            visited[to] = True
            answer += cost
            
            for next_to, next_c in island[to]:
                if not visited[next_to]:
                    heapq.heappush(heap,(next_c,next_to))
    
    return answer