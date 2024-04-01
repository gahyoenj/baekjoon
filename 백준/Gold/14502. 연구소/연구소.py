from collections import deque
import copy
def cnt(arr):
    no_virus = 0
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 0:
                no_virus += 1
    return no_virus


def bfs(lst):
    global maxV
    temp = copy.deepcopy(arr)
    q = deque()
    visited = [[0]*M for _ in range(N)]
    for row,col in lst:
        visited[row][col] = 1
        q.append((row,col))

    while q:
        vr,vc = q.popleft()

        for dr,dc in [(1,0),(0,1),(0,-1),(-1,0)]:
            nr = vr+dr
            nc = vc+dc
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and temp[nr][nc] == 0:
                visited[nr][nc] = visited[vr][vc] + 1
                q.append((nr,nc))
                temp[nr][nc] = 2
    maxV =max(cnt(temp),maxV)
def combi(k,n):
    if k == 3:
        lst = []
        for num in result:
            lst.append(blank[num])
        # print(lst)
        for r,c in lst:
            arr[r][c] = 1
        bfs(virus)
        for r,c in lst:
            arr[r][c] = 0
        return

    for i in range(n,len(blank)):
        result[k] = i
        combi(k+1,i+1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

blank = []
virus = []
for row in range(N):
    for col in range(M):
        if arr[row][col] == 0:
            blank.append((row,col))
        if arr[row][col] == 2:
            virus.append((row,col))
result = [-1] * 3
maxV = 0
combi(0,0)
print(maxV)
