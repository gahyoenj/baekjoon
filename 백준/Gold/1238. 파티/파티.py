import heapq
def party(start,end,visited,arrive):
    q = []
    heapq.heappush(q,(visited[start],start))

    while q:
        pre_time, next = heapq.heappop(q)
        if next == end and not arrive:
            arrive = True

        if next == end and arrive:
            # print(start,visited)
            return visited[end]

        for node, t in G[next]:
            time = t + visited[next]
            if time < visited[node]:
                # print(visited)
                visited[node] = time
                heapq.heappush(q,(time,node))
    # return visited[i]+visited[X]

N,M,X = map(int,input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,t = map(int,input().split())
    G[s].append((e,t))

maxV = 0
for i in range(1,N+1):
    if i != X:
        arrive = False
        visited = [1e9] * (N + 1)
        visited[i] = 0
        go = party(i,X,visited,arrive)
        visited = [1e9] * (N + 1)
        visited[X] = 0
        arrive = True
        back = party(X,i,visited,arrive)
        if go+back > maxV:
            maxV = go+back
print(maxV)
