N, M = map(int,input().split())

def kb(person):
    global minX , minP
    visited = [-1] * (N+1)
    q = []
    q.append(person)
    visited[person] = 0

    while q:
        p = q.pop(0)

        for friend in G[p]:
            if visited[friend] == -1:
                visited[friend] = visited[p] + 1
                q.append(friend)
    # print(sum(visited))

    kevin = sum(visited) + 1
    if minX >= kevin:
        minX = kevin
        minP = person

G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

minX = 100000000
minP = ''

for i in range(N,0,-1):
    kb(i)

print(minP)