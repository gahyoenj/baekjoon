import sys
sys.setrecursionlimit(500000)
def dfs(node):
    visited[node] = True

    for v in G[node]:
        if not visited[v]:
            count[v] = count[node] + 1
            dfs(v)

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# print(G)
visited = [False] * (N+1)
leaf = []
for node in range(2,N+1):
    if len(G[node]) == 1:
        leaf.append(node)

count = [0] * (N+1)
# print(leaf)
dfs(1)
ans = 0
for i in leaf:
    ans += count[i]
# print(ans)
if ans % 2 == 0:
    print('No')
else:
    print('Yes')