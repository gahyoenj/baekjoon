N = int(input())

child = [0]
for _ in range(N):
    i = int(input())
    child.append(i)

dp = [1] * (N+1)

for i in range(1,N+1):
    for j in range(1,i):
        if child[i] > child[j]:
            dp[i] = max(dp[i],dp[j]+1)

ans = N- max(dp)
print(ans)