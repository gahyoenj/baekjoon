from collections import deque
def bfs(start):
    q = deque([start])
    visited = [-1] * 101
    visited[start] = 0

    while q:
        current = q.popleft()
        if current == 100:
            return visited[current]

        for i in range(1,7):
            next = current + i
            if next <= 100 and visited[next] == -1:
                if next in ladder.keys():
                    next = ladder[next]
                if next in snake.keys():
                    next = snake[next]
                if visited[next] == -1:
                    visited[next] = visited[current] + 1
                    q.append(next)


N,M = map(int,input().split())

ladder = {}
for _ in range(N):
    x,y = map(int,input().split())
    ladder[x] = y


snake = {}
for _ in range(M):
    u,v = map(int,input().split())
    snake[u] = v

print(bfs(1))
