from collections import deque

def dfs(s):
    visited[s] = 1
    print(s, end=' ')
    for i in G[s]:
        if not visited[i]:
            dfs(i)



def bfs(s):
    q = deque()
    visited = [0] * (N+1)
    q.append(s)
    visited[s] = 1

    while q:
        v = q.popleft()
        print(v,end=' ')
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1


N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    v1,v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

for idx in range(N+1):
    G[idx].sort()


visited = [0] * (N+1)
dfs(V)
print()
bfs(V)