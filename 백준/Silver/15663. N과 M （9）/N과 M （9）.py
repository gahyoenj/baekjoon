def dfs():
    if len(ans) == M:
        print(*ans)
        return

    check = 0
    for i in range(N):
        if not visited[i] and check != arr[i]:
            ans.append(arr[i])
            visited[i] = True
            check = arr[i]
            dfs()
            visited[i] = False
            ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = [-1] * M
visited = [False] * N
arr.sort()
ans = []
dfs()

