def check(start,n):
    global lst,cnt
    q = [n]
    visited = [False] * (N + 1)
    visited[n] = True

    while q:
        v = q.pop()
        if v == start:
            cnt += 1
            lst.append(v)
            return

        for node in G[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True


N = int(input())

G = [[] for _ in range(N+1)]

for idx in range(N):
    n = int(input())
    G[idx+1].append(n)

lst = []
cnt = 0


for i in range(1,N+1):
    check(i,G[i][0])

print(cnt)
for num in lst:
    print(num)