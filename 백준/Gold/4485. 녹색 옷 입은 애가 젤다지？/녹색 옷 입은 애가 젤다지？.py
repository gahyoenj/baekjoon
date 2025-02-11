import heapq
def bfs(row,col):
    visited = [[1e9]*N for _ in range(N)]
    visited[row][col] = dongul[row][col]
    q = [(dongul[row][col],row,col)]

    while q:
        cost, vr,vc = heapq.heappop(q)
        if vr == N-1 and vc == N-1:
            # print(visited)
            return visited[vr][vc]

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            newR = vr + dr
            newC = vc + dc
            if 0<=newR<N and 0<=newC<N:
                lost = cost + dongul[newR][newC]
                if lost < visited[newR][newC]:
                    heapq.heappush(q,(lost,newR,newC))
                    visited[newR][newC] = lost
T = 1
while True:

    N = int(input())
    if N == 0:
        break
    else:
        dongul = [list(map(int,input().split())) for _ in range(N)]
        ans = bfs(0,0)
        print(f'Problem {T}: {ans}')
        T += 1