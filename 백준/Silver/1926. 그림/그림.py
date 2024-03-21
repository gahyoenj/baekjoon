def bfs(row,col):
    cnt = 1
    q = []
    q.append((row,col))
    arr[row][col] = -1
    while q:
        vr,vc = q.pop(0)

        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            newR = vr + dr
            newC = vc + dc
            if 0<=newR<n and 0<=newC<m and arr[newR][newC]==1:
                arr[newR][newC] = -1
                q.append((newR,newC))
                cnt += 1
    return cnt


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

lst = []
for row in range(n):
    for col in range(m):
        if arr[row][col] == 1:
            lst.append(bfs(row,col))
if lst:
    print(len(lst))
    print(max(lst))
else:
    print(len(lst))
    print(0)