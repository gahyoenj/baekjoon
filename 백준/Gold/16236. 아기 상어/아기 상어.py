def fish_eat():
    check = False
    global eat,shark,ans
    now = 21e9
    er = 0
    ec = 0
    for row in range(N):
        for col in range(N):
            if 0< arr[row][col] < shark and ans[row][col] < now:
                now = ans[row][col]
                er = row
                ec = col

    eat += 1
    arr[er][ec] = 0
    if shark == eat:
        shark += 1
        eat = 0

    return ans[er][ec] ,er,ec

# def can_eat():
#     global ans
#     flag = False
#     for row in range(N):
#         for col in range(N):
#             if 0< arr[row][col] < shark:
#                 flag =True
#     return flag

def bfs(sr,sc):
    can_eat = False
    visited = [[21e9] * N for _ in range(N)]
    global shark
    q = [(sr,sc)]
    visited[sr][sc] = 0

    while q:
        vr,vc = q.pop(0)

        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            newR = vr + dr
            newC = vc + dc
            if 0<=newR<N and 0<=newC<N and visited[vr][vc] + 1 < visited[newR][newC]:
                if arr[newR][newC] <= shark:
                    visited[newR][newC] = visited[vr][vc] + 1
                    q.append((newR,newC))
                    if 0<arr[newR][newC]<shark:
                        can_eat = True
    return visited,can_eat
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = 2
cnt = 0
sr = 0
sc = 0
for row in range(N):
    for col in range(N):
        if arr[row][col] == 9:
            arr[row][col] = 0
            sr = row
            sc = col
eat = 0
time = 0
while True:
    ans,flag = bfs(sr,sc)
    if not flag:
        break
    t,sr,sc = fish_eat()
    time += t


print(time)