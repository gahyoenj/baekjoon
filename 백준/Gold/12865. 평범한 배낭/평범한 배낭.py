N, K = map(int,input().split())
bag = []
for _ in range(N):
    w, v = map(int,input().split())
    bag.append((w,v))

dp = [0] * (K+1)
for item in bag:
    weight, value = item
    for i in range(K,weight-1,-1):
        dp[i] = max(dp[i],dp[i-weight]+value)

print(dp[-1])