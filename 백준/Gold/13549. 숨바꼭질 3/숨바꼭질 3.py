from collections import deque
N, K = map(int,input().split())

visited = [21e9] * 100001
visited[N] = 0

q = deque([N])

while q:
    x = q.popleft()
    if x == K:
        print(visited[x])
        break

    if 0<=2*x<=100000 and visited[2*x] > visited[x]:
        visited[2*x] = visited[x]
        q.append(2*x)

    for next in [x-1,x+1]:
        if 0<=next<=100000 and visited[next] > visited[x]+1:
            visited[next] = visited[x]+1
            q.append(next)
