from collections import deque
def bfs(row,col):
    global cnt
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((row,col,cnt))
    visited[row][col][cnt] = 1

    while q:
        vr,vc,cnt = q.popleft()
        if vr==N-1 and vc==M-1:
            # print(visited[vr][vc])
            return visited[vr][vc][cnt]

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            newR = vr + dr
            newC = vc + dc
            if 0<= newR < N and 0<=newC<M and not visited[newR][newC][cnt]:
                if arr[newR][newC] == '0':
                    q.append((newR,newC,cnt))
                    visited[newR][newC][cnt] = visited[vr][vc][cnt] + 1
                elif arr[newR][newC] =='1' and cnt < 1:
                    q.append((newR,newC,cnt+1))
                    visited[newR][newC][cnt+1] = visited[vr][vc][cnt] + 1


    return -1

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

cnt = 0   # 벽부수는 횟수

print(bfs(0,0))