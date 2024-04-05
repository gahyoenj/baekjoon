def bfs(row,col):
    global maxV
    visited = [[0] * C for _ in range(R)]
    q = []
    q.append((row,col))
    visited[row][col] = 1

    while q:
        vr,vc = q.pop(0)

        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            newR = vr + dr
            newC = vc + dc
            if 0<= newR < R and 0<=newC<C and not visited[newR][newC] and arr[newR][newC] == 'L':
                visited[newR][newC] = visited[vr][vc] + 1
                q.append((newR,newC))
                maxV = max(maxV,visited[newR][newC])



R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
maxV = 0
for row in range(R):
    for col in range(C):
        if arr[row][col] == 'L':
            bfs(row,col)
print(maxV-1)