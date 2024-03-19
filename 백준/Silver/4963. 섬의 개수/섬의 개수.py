import sys
sys.setrecursionlimit(10**5)
def dfs(row,col):
    if row == w and col == h:
        return

    global cnt
    visited[row][col] = True
    if MAP[row][col] == 1:
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
            newR = row + dr
            newC = col +dc
            if 0<= newR < h and 0 <= newC < w and not visited[newR][newC] and MAP[newR][newC] == 1:
                visited[newR][newC] = True
                dfs(newR,newC)




while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0 :break
    MAP = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for row in range(h):
        for col in range(w):
            if MAP[row][col] == 1:
                if not visited[row][col]:
                    dfs(row,col)
                    cnt += 1
    print(cnt)