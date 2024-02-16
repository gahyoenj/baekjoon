import sys
def bfs(s):
  q = []

  q.append(s)
  visited[s] = True

  while q:
    v = q.pop(0)
    # print(v)

    for w in G[v]:
      if not visited[w]:
        q.append(w)
        visited[w] = True

N , M = map(int, sys.stdin.readline().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  G[u].append(v)
  G[v].append(u)
visited = [False]*(N+1)
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt+=1
print(cnt)