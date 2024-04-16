from collections import deque

def bfs(lst):
    q = deque()
    for i in lst:
        q.append(i)

    while q:
        h, vr, vc = q.popleft()

        for dh,dr,dc in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
            newh = h + dh
            newR = vr + dr
            newC = vc + dc
            if 0<=newh<H and 0<=newR<N and 0<=newC<M and not visited[newh][newR][newC]:
                if visited[newh][newR][newC] == 0:
                    q.append((newh,newR,newC))
                    visited[newh][newR][newC] = visited[h][vr][vc] + 1






M, N ,H = map(int,input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# print(arr)
lst = []
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

for h in range(H):
    for row in range(N):
        for col in range(M):
            if arr[h][row][col] == 1:
                visited[h][row][col] = 1
                lst.append((h,row,col))
            if arr[h][row][col] == -1:
                visited[h][row][col] = 1

bfs(lst)
maxV = 0
for h in range(H):
    for row in range(N):
        for col in range(M):
            if visited[h][row][col] > maxV:
                maxV = visited[h][row][col]
            if visited[h][row][col] == 0:
                print(-1)
                exit()

print(maxV-1)

