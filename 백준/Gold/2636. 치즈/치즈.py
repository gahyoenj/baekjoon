def check(lst):
    global cheese_cnt
    for row in range(r):
        for col in range(c):
            if cheese[row][col] == 1:
                cheese_cnt += 1

    return cheese_cnt

def bfs(row,col):
    visited = [[False] * c for _ in range(r)]
    q = []
    visited[row][col] = True
    q.append((row, col))

    while q:
        vr,vc = q.pop(0)

        for dr,dc in [(-1,0),(0,1),(0,-1),(1,0)]:
            newR = vr + dr
            newC = vc + dc
            if 0<=newR<r and 0<= newC<c:
                if cheese[newR][newC] == 0 and not visited[newR][newC]:
                    q.append((newR,newC))
                    visited[newR][newC] = True
                elif cheese[newR][newC] == 1 and not visited[newR][newC]:
                    cheese[newR][newC] = 0
                    visited[newR][newC] = True



r,c = map(int, input().split())
cheese = [list(map(int ,input().split())) for _ in range(r)]

time = 0
cheese_lst = []
while True:
    cheese_cnt = 0
    if check(cheese) > 0:
        cheese_lst.append(cheese_cnt)
        bfs(0,0)
        time += 1

    if check(cheese) == 0:
        break


print(time)
print(cheese_lst[-1])
