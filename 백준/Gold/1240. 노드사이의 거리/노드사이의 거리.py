def dfs(node,d):
    visited[node] = True
    if node == n2:
        print(d)
        return

    for next,dis in G[node]:
        if not visited[next]:
            dfs(next,d+dis)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    v1, v2, distance = map(int, input().split())
    G[v1].append((v2,distance))
    G[v2].append((v1,distance))


for _ in range(M):
    n1, n2 = map(int, input().split())
    d = 0
    visited = [False] * (N+1)
    dfs(n1,d)