from collections import deque
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]


def bfs(row, col):

    visited = [[-1] * M for _ in range(N)]
    queue = deque([(row, col)])
    visited[row][col] = 0

    while queue:
        r, c = queue.popleft()


        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1 and MAP[nr][nc] == 1:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))

    return visited


tr, tc = -1, -1
for row in range(N):
    for col in range(M):
        if MAP[row][col] == 2:
            tr, tc = row, col
            break

result = bfs(tr, tc)

for row in range(N):
    for col in range(M):
        if MAP[row][col] == 0:
            result[row][col] = 0

for row in result:
    print(*row)
