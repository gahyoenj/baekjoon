def graph(i):
    pay = [1e9] * (N+1)
    pay[i] = 0
    q = [i]
    minV = 2e10
    while q:
        next = q.pop(0)
        if next == N and minV > pay[N]:
            minV = pay[N]

        for node, cost in G[next]:
            next_cost = cost + pay[next]
            if next_cost < pay[node]:
                pay[node] = next_cost
                q.append(node)
    return minV

N,M = map(int,input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    v1,v2,cost = map(int,input().split())
    G[v1].append((v2,cost))
    G[v2].append((v1,cost))

print(graph(1))