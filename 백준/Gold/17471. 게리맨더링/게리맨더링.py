from collections import deque


def bfs(s, group, G):
    visited = [False] * (len(G) + 1)
    q = deque([s])
    visited[s] = True
    vote = []

    while q:
        node = q.popleft()
        vote.append(node)
        for neighbor in G[node]:
            if neighbor in group and not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

    return set(vote) == set(group)


def subset(k, A):
    global minV
    if k == N + 1:
        if len(A) > 0 and len(A) < N:
            B = list(set(range(1, N + 1)) - set(A))
            sumA = sum(people[node - 1] for node in A)
            sumB = sum(people[node - 1] for node in B)

            if bfs(A[0], A, G) and bfs(B[0], B, G):
                minV = min(minV, abs(sumA - sumB))
        return

    subset(k + 1, A)  # Not including k-th region in A
    subset(k + 1, A + [k])  # Including k-th region in A


N = int(input())
people = list(map(int, input().split()))

G = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    lst = list(map(int, input().split()))
    num = lst[1:]
    for j in range(lst[0]):
        G[i].append(num[j])

minV = 1001
subset(1, [])
if minV == 1001:
    print(-1)
else:
    print(minV)
