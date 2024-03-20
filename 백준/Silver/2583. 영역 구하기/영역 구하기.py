def bfs(row,col):
    cnt = 1
    q = []
    q.append((row,col))
    arr[row][col] = 1

    while q:
        vr,vc = q.pop(0)
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            newR = vr + dr
            newC = vc + dc
            if 0<= newR < M and 0<= newC < N and arr[newR][newC] == 0:
                q.append((newR,newC))
                arr[newR][newC] = 1
                cnt += 1
    return cnt

M,N,K = map(int,input().split())
arr = [[0]*N for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for col in range(x1,x2):
        for row in range(y1,y2):
            arr[row][col] = 1
# print(arr)   # 문제에 주어진 그림 뒤집은 모양으로 나옴 /(0,0)이 좌측하단이 아니라 좌측상단으로 바뀜
lst = []
for row in range(M):
    for col in range(N):
        if arr[row][col] == 0:
            lst.append(bfs(row,col))
lst.sort()
print(len(lst))
print(*lst)