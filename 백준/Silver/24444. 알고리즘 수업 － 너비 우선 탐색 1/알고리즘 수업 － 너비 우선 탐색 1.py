import sys
input = sys.stdin.readline
from collections import deque
def bfs(node):
    global order
    visited[node] = True
    q= deque()
    q.append(node)

    while q:
        v = q.popleft()

        for next in G[v]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                order += 1
                ans[next] = order


    return ans
N,M,R = map(int,input().split())
G = [[]for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
for i in range(N+1):
    G[i].sort()
# print(G)
visited = [False] * (N+1)
order = 1
ans = [0] * (N+1)
ans[R] = order
result = bfs(R)

for i in result[1::]:
    print(i)
