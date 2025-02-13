from collections import deque
import sys
input = sys.stdin.readline 
def bfs(row,col):
    global ans
    visited = [[0]*M for _ in range(N)]
    height = land[row][col]
    minV = 10
    q = deque([(row,col)])
    visited[row][col] = 1
    pool = [(row,col)]

    while q:
        vr,vc = q.popleft()

        for dr,dc in [(1,0),(0,1),(0,-1),(-1,0)]:
            newR = vr + dr
            newC = vc + dc
            if newR<=-1 or newR>=N or newC<=-1 or newC>=M:
                return
            if 0<=newR<N and 0<=newC<M and not visited[newR][newC]:
                if height >= land[newR][newC]:
                    q.append((newR,newC))
                    pool.append((newR,newC))
                    visited[newR][newC] = 1
                else:
                    minV = min(minV,land[newR][newC])
    for pr,pc in pool:
        ans += (minV - land[pr][pc])
        land[pr][pc] = minV


N,M = map(int,input().split())

land = [list(map(int, input().rstrip())) for _ in range(N)]
ans = 0
# print(land)

for row in range(1,N-1):
    for col in range(1,M-1):
        bfs(row,col)
print(ans)