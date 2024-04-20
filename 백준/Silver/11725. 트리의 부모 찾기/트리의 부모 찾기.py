import sys
sys.setrecursionlimit(10**6)
def dfs(node):
    for v in G[node]:
        if not visited[v]:
            p[v] = node
            visited[v] = True
            dfs(v)

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    v1,v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)
# print(G)
visited = [False] * (N+1)
p = [0] * (N+1)
visited[1] = True
dfs(1)

# print(p)
for i in range(2,N+1):
    print(p[i])