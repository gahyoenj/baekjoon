def clean(r,c,d):
    global cnt
    if arr[r][c] == 0:
        cnt += 1
        arr[r][c] = 2

    for _ in range(4):
        nd = (d+3) % 4 # 반시계방향으로 돌기
        row = r + direction[nd][0]
        col = c + direction[nd][1]
        if arr[row][col] == 0:
            clean(row,col,nd)
            return
        d = nd


    nd = (d+2) % 4 # 후진
    row = r + direction[nd][0]
    col = c + direction[nd][1]
    if arr[row][col] != 1:
        clean(row,col,d)
    else:
        return


n,m = map(int, input().split())
r,c,d = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]
direction = [(-1,0),(0,1),(1,0),(0,-1)] # 북동남서
cnt = 0
clean(r,c,d)
print(cnt)