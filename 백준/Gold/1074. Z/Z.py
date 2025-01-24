N,r,c = map(int, input().split())

def z(row,col,n):
    global cnt
    if row == r and col == c:
        print(cnt)
        exit()

    if n == 1:
        cnt += 1
        return

    if not (row <= r < row + n and col <= c < col +n):
        cnt += n * n
        return

    z(row,col,n//2)
    z(row,col+n//2,n//2)
    z(row+n//2,col,n//2)
    z(row+n//2,col+n//2,n//2)

size = 2 ** N
cnt = 0
z(0,0,size)