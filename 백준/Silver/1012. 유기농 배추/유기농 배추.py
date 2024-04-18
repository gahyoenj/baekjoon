def bfs(row,col):
    q = []
    q.append((row,col))
    visited[row][col] = True

    while q:
        vr,vc = q.pop(0)

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            newR = vr + dr
            newC = vc + dc
            if 0<=newR<N and 0<=newC<M and not visited[newR][newC] and arr[newR][newC] == 1:
                q.append((newR,newC))
                visited[newR][newC] = True

T = int(input())
for tc in range(T):
    M,N,K = map(int ,input().split())
    arr = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x,y = map(int, input().split())
        arr[y][x] = 1
    visited = [[False]*M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1 and not visited[row][col]:
                bfs(row,col)
                cnt += 1
    print(cnt)