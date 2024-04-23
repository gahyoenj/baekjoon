import sys
input = sys.stdin.readline

def travel(node):
    global flight
    country.append(node)
    flight += 1
    if len(country) == N:
        return

    for i in G[node]:
        if i not in country:
            travel(i)

T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    # print(G)
    country = []
    flight = 0
    travel(1)
    print(flight-1)