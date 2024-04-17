def bfs(row,col,color):
    q = []
    q.append((row,col,color))

    while q:
        vr,vc,C = q.pop(0)
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            newR = vr + dr
            newC = vc + dc
            if 0<= newR < N and 0<=newC < N and not visited[newR][newC] and arr[newR][newC] == C:
                q.append((newR,newC,arr[newR][newC]))
                visited[newR][newC] = True
N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
cnt = 0
c = ['R','G','B']
for row in range(N):
    for col in range(N):
        for cl in c:
            if arr[row][col] == cl and not visited[row][col]:
                bfs(row,col,cl)
                cnt += 1

cnt_g = 0
visited = [[False] * N for _ in range(N)]
for row in range(N):
    for col in range(N):
        if arr[row][col] == 'G':
            arr[row][col] = 'R'

c = ['R','B']
for row in range(N):
    for col in range(N):
        for cl in c:
            if arr[row][col] == cl and not visited[row][col]:
                bfs(row,col,cl)
                cnt_g += 1

print(cnt, cnt_g)