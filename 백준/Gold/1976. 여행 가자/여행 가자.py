def travel(node):
    global visited
    q =[node]
    visited[node] = True

    while q:
        v = q.pop(0)

        for n in route[v]:
            if not visited[n]:
                q.append(n)
                visited[n] = True


N = int(input())
M = int(input())

route = [[] for _ in range(N+1)]

for i in range(N):
    info = list(map(int,input().split()))
    for j in range(len(info)):
        if info[j] == 1:
            route[i+1].append(j+1)


plan = list(map(int,input().split()))

visited = [False] * (N + 1)

travel(plan[0])

for i in plan:
    if not visited[i]:
        print('NO')
        exit()

print('YES')