def perm(k):
    if k == M:
        print(*result[:M])
        return

    for i in range(1,N+1):
        if not visited[i]:
            result[k] = i
            visited[i] = True
            perm(k+1)
            visited[i] = False

N, M = map(int, input().split())
visited = [False] * (N+1)
result = [-1] * (N+1)
perm(0)