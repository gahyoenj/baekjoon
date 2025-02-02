def solution(n, wires):
    def bfs(s,e,visited):
        cnt = 1
        q = [e]
        
        while q:
            v = q.pop(0)
            for node in G[v]:
                if not visited[node]:
                    cnt += 1
                    visited[node] =True
                    q.append(node)
        return cnt
    
    answer = -1
    G = [[] for _ in range(n+1)]
    for v1,v2 in wires:
        G[v1].append(v2)
        G[v2].append(v1)
    
    minV = 10000000
    for s,e in wires:
        visited = [False] * (n+1)
        visited[s] =True
        visited[e] =True
        node_cnt = bfs(s,e,visited)
        
        if minV > abs(n-2*node_cnt):
            minV = abs(n-2*node_cnt)
    
    return minV