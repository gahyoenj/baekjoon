def dfs(row, col):
    stack = []
    stack.append((row,col))
    visited[row][col] = True

    while stack:
        r, c = stack.pop()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newR = r + dr
            newC = c + dc

            if 0 <= newR < N and 0 <= newC < N and not visited[newR][newC]:
                stack.append((newR, newC))
                visited[newR][newC] = True


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_height = max(map(max,arr))
maxV = 0
for i in range(max_height):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] <= i:
                visited[row][col] = True

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                cnt += 1
                dfs(r, c)
    if cnt > maxV:
        maxV = cnt

print(maxV)