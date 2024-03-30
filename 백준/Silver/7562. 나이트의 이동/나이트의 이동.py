def bfs(row,col):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((row,col))
    visited[row][col] = 1

    while q:
        vr,vc = q.pop(0)
        if vr == ar and vc == ac:
            return visited[vr][vc]

        for dr,dc in [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]:
            newR = dr + vr
            newC = dc + vc

            if 0<=newR<N and 0<=newC<N and not visited[newR][newC]:
                q.append((newR,newC))
                visited[newR][newC] = visited[vr][vc] + 1


T = int(input())
for _ in range(T):
    N = int(input())
    chess = [[0] * N for _ in range(N)]
    now_r,now_c = map(int, input().split())
    ar,ac = map(int, input().split())
    chess[ar][ac] = 1
    print(bfs(now_r,now_c)-1)
