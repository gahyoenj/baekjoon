def dfs(node):
    visited[node] = True
    # print(node)

    for i in G[node]:
        if not visited[i]:
            dfs(i)
            G[i].append(-1)

N = int(input())
arr = list(map(int, input().split()))
delete_node = int(input())

G = [[] for _ in range(N)]

for idx in range(N):
    if arr[idx] != -1:
        G[arr[idx]].append(idx)
        # G[idx].append(arr[idx])
# print(G)
visited = [False] * N
dfs(delete_node)
G[delete_node].append(-1)
# print(G)
ans = 0

for sub in range(N):
    for idx in range(len(G[sub])):
        if G[sub][idx] == delete_node:
            G[sub].remove(delete_node)
            break
    if len(G[sub]) == 0:
        ans += 1

print(ans)