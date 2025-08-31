def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n+1)]
    
    for v1,v2 in roads:
        graph[v1].append(v2)
        graph[v2].append(v1)
    

    result = -1
    visited = [-1] * (n+1)
    q = [destination]
    visited[destination] = 0


    while q:
        s = q.pop(0)

        for v in graph[s]:
            if visited[v] == -1:
                q.append(v)
                visited[v] = visited[s] + 1
    
    for start in sources:
        answer.append(visited[start])

            
            
    
    return answer