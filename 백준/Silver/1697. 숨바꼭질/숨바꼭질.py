N,K = map(int,input().split())

visited = [-1] * 100001

visited[N] = 0

q = [N]

while q:
    now = q.pop(0)
    if now == K:
        print(visited[K])
        break

    x = now-1
    if 0<= x <= 100000 and visited[x] == -1:
        q.append(x)
        visited[x] = visited[now] + 1
    y = now + 1
    if 0<= y <= 100000 and visited[y] == -1:
        q.append(y)
        visited[y] = visited[now] + 1
    z = now * 2
    if 0<= z <= 100000 and visited[z] == -1:
        q.append(z)
        visited[z] = visited[now] + 1


