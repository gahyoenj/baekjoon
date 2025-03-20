n = int(input())
m = int(input())

cost = [[2e19]*n for _ in range (n)]
for i in range(n):
    for j in range(n):
        if i==j:
            cost[i][j] = 0


for _ in range(m):
    a,b,c = map(int,input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

for i in range(n):
    for j in range(n):
        if cost[i][j] == 2e19:
            cost[i][j] = 0


for i in range(n):
    print(*cost[i])