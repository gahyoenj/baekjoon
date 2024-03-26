def people(move):
    sumV = 0
    k = len(move)


    for dr,dc in move:
        sumV += arr[dr][dc]

    for dr,dc in move:
        arr[dr][dc] = int(sumV / k)


def bfs(row,col,move):
    q = []
    q.append((row,col))
    move.append((row,col))
    while q:
        vr,vc = q.pop()

        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            newR = vr+dr
            newC = vc+dc
            if 0<=newR<N and 0<=newC<N and not visited[newR][newC]:
                if L <= abs(arr[newR][newC] - arr[vr][vc]) <=R:
                    visited[newR][newC] = 1
                    q.append((newR,newC))
                    move.append((newR,newC))



N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    moved = False
    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                visited[row][col] = 1
                move = []
                bfs(row,col,move)
                if len(move) > 1:
                    moved = True
                    people(move)

    if not moved:
        break
    cnt += 1

print(cnt)
