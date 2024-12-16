def check(s):
    q = []
    
    q.append(s)
    visited[s] = 1
    
    while q:
        v = q.pop(0)
        
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1

def solution(n, computers):
    answer = 0
    global visited
    visited = [0] * (n+1)
    global G
    G = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i!=j:
                G[i+1].append(j+1)
    # print(G)
    for i in range(1,n+1):
        if not visited[i]:
            check(i)
            answer += 1
    return answer