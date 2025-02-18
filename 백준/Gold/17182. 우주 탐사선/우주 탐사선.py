def dfs(node,cnt,time):
    global minV

    if cnt == N:
        minV = min(minV,time)
        return

    for next in range(N):
        if not visited[next]:
            visited[next] = True
            dfs(next,cnt+1,time+arr[node][next])
            visited[next] = False


N, K = map(int,input().split())

arr = [list(map(int,input().split()))for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j : continue
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

minV = 21e9
visited = [False] * N
visited[K] = True
dfs(K,1,0)

print(minV)