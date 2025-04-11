def dijkstra(s):
    cost[s] = 0
    st = [(s,0)]

    while st:
        v,c = st.pop()

        if cost[v] < c:
            continue

        for node in bus[v]:
            if c+ node[1] < cost[node[0]]:
                cost[node[0]] = c + node[1]
                st.append((node[0],cost[node[0]]))


n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,c = map(int,input().split())
    bus[s].append((e,c))
s,e = map(int,input().split())

cost = [2e19] * (n+1)

dijkstra(s)
print(cost[e])
