#7576
from collections import deque

def tomato(lst):
    global cnt
    q =deque()
    visited = [[0] * M for _ in range(N)]
    for i in range(len(lst)):
        q.append(lst[i])
        visited[lst[i][0]][lst[i][1]] = 1

    while q:
        row,col = q.popleft()

        for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            newR = row + dr
            newC = col + dc
            if 0 <= newR < N and 0 <= newC < M and not visited[newR][newC] and arr[newR][newC] == 0:
                arr[newR][newC] = 1
                visited[newR][newC] += (visited[row][col]+1)
                q.append((newR,newC))
    return visited



M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
lst = []
for row in range(N):
    for col in range(M):
        if arr[row][col] == 1:
            str = row
            stc = col
            lst.append((str,stc))
visited = tomato(lst)

# print(visited)
cnt = 0
for row in range(N):
    for col in range(M):
        if arr[row][col] == 0:
            cnt += 1

if cnt !=0 :
    print(-1)
else:
    maxV = 0
    for row in range(N):
        for col in range(M):
            if visited[row][col] > maxV:
                maxV = visited[row][col]
    print(maxV-1)



# print(cnt)
# print(arr)
