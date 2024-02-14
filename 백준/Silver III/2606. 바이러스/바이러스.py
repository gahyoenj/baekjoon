def dfs(k):
  STACK = []
  visited = [False] * (N+1)
  STACK.append(k)
  visited[k] = True
  lst=[]
  while STACK:
    v = STACK.pop()
    lst.append(v)
  
    for w in G[v]:
      if not visited[w]:
        STACK.append(w)
        visited[w] = True
  return len(lst)

N = int(input())
c = int(input())
G = [[] for _ in range(N+1)]

for _ in range(c):
  i, j = map(int, input().split())
  G[i].append(j)
  G[j].append(i)
# print(G)
print(dfs(1)-1)