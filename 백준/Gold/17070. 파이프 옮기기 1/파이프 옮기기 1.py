import sys
input = sys.stdin.readline
def dfs(r,c,direction):
    global cnt

    if r == N-1 and c == N-1:
        cnt += 1
        return

    if direction == 0 or direction==2:
        if c + 1 < N and arr[r][c+1] == 0:
            dfs(r,c+1,0)  # 가로로 이동
    if direction == 1 or direction == 2:
        if r + 1 < N and arr[r+1][c] == 0:
            dfs(r+1,c,1)  # 세로로 이동
    if direction == 0 or direction == 1 or direction==2:
        if r+1<N and c+1<N and arr[r+1][c+1] == 0 and arr[r+1][c] == 0 and arr[r][c+1]==0:
            dfs(r+1,c+1,2)  # 대각선 이동



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0


dfs(0,1,0)
print(cnt)