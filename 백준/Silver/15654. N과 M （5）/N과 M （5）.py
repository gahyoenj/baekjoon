def perm(k):
    if k == M:
        print(*result)
        return

    for i in range(0,N):
        if not visited[i]:
            result[k] = num[i]
            visited[i] = True
            perm(k+1)
            visited[i] =False




N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
visited = [False] * (N+1)
result = [-1] * M
perm(0)