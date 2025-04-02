N, D = map(int,input().split())

route = {}
for _ in range(N):
    s, e, l = map(int,input().split())
    if e > D:
        continue
    if (s,e) in route:
        route[(s,e)] = min(route[(s,e)], l)
    else:
        route[(s,e)] = l
# print(route)

dp = [2e19] * (D+1)
dp[0] = 0

for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1] + 1)

    for (s,e), l in route.items():
        if i == s:
            dp[e] = min(dp[e], dp[s] + l)

print(dp[D])