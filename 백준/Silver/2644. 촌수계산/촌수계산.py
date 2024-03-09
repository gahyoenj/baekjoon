def dfs(s,e):
    st = []
    visited = [False] * (n+1)
    st.append((s,0))
    visited[s] = True

    while st:
        v1,cnt = st.pop(0)
        # cnt += 1
        # print(v1)
        if v1 == e:
            return cnt
        for w in G[v1]:
            if not visited[w]:
                st.append((w,cnt+1))
                visited[w] = True
    return -1

n = int(input())
p1, p2 = map(int, input().split())
# if p1 > p2:
#     p1, p2 = p2, p1
m = int(input())
G = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

print(dfs(p1,p2))
