
    

def solution(n, edge):
    answer = 0
    G = [[] for _ in range(n+1)]
    node = {}
    for i in range(0,n+1):
        node[i] = 0
    for v1,v2 in edge:
        G[v1].append(v2)
        G[v2].append(v1)
    # print(G)
    
    q = [1]
    visited = [0] * (n+1)
    visited[1] = 1
    visited[0] = 1
    
    while q:
        v = q.pop(0)
        
        for node in G[v]:
            if visited[node] == 0:
                visited[node] += visited[v] +1
                q.append(node)
    maxV = max(visited)
    answer = visited.count(maxV)
    return answer