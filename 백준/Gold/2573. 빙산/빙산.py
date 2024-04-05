from collections import deque
def bfs(row,col):
    q = deque()
    q.append((row,col))
    visited[row][col] = True

    while q:
        vr,vc = q.popleft()

        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            newR = vr+dr
            newC = vc +dc
            if 0<=newR<N and 0<=newC<M and not visited[newR][newC]:
                if arr[newR][newC] == 0:
                    arr[vr][vc] -= 1
                else:
                    q.append((newR,newC))
                    visited[newR][newC] = True
        if arr[vr][vc] < 0:
            arr[vr][vc] = 0

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
year = 0
ice = []
for row in range(N):
    for col in range(M):
        if arr[row][col] != 0:
            ice.append((row,col))
while ice:
    ans = 0
    melted = []
    visited = [[False] * M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if arr[row][col]!=0 and not visited[row][col]:
                bfs(row,col)
                ans += 1
            if arr[row][col] == 0:
                melted.append((row,col))

    if ans >=2:
        print(year)
        break
    year += 1
    ice = list(set(ice) - set(melted))

if ans < 2:
    print(0)
