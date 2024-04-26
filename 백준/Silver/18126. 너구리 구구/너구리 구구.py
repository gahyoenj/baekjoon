def bfs(node):
    q = []
    q.append(node)
    visited[node] = 1

    while q:
        v = q.pop(0)
        for i,len in G[v]:
            if not visited[i]:
                visited[i] = visited[v] + len
                q.append(i)

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))
visited = [0] * (N+1)

bfs(1)
# print(visited)
print(max(visited)-1)