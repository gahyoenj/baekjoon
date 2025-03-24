N, K = map(int,input().split())

visited = [-1] * 100001
ways = [0] * 100001
visited[N] = 0

q = [N]
ways[N] = 1
cnt = 0

while q:
    next = q.pop(0)
    if next == K:
        print(visited[next])
        print(ways[next])
        break


    for i in [next-1,next+1,next*2]:
        if i == K:
            cnt += 1
        if 0<= i <= 100000:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[next] + 1
                ways[i] = ways[next]
            elif visited[i] == visited[next] + 1:
                ways[i] += ways[next]