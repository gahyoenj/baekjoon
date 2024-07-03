def bfs(row,col):
    q = []
    q.append((row,col))

    while q:
        vr,vc = q.pop(0)
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            newR = vr + dr
            newC = vc + dc
            if 0<=newR<N and 0<=newC<M and arr[newR][newC]==0:
                q.append((newR,newC))
                arr[newR][newC] = 1
            if newR < 0 and newR == -1 and arr[N-1][newC] == 0:
                q.append((N-1,newC))
                arr[N-1][newC] = 1
            if newC < 0 and newC == -1 and arr[newR][M-1] == 0:
                q.append((newR,M-1))
                arr[newR][M-1] = 1
            if newR > N-1 and newR == N and arr[0][newC] == 0:
                q.append((0,newC))
                arr[0][newC] = 1
            if newC > M-1 and newC == M and arr[newR][0] == 0:
                q.append((newR,0))
                arr[newR][0] = 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


cnt = 0
for row in range(N):
    for col in range(M):
        if arr[row][col] == 0:
            bfs(row,col)
            cnt += 1

print(cnt)