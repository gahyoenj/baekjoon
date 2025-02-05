import sys
input = sys.stdin.readline

N =int(input())
Ai = list(map(int,input().split()))

dp = [1] * (N+1)

for i in range(1,N):
    for j in range(i):
        if Ai[i] > Ai[j]:
            dp[i] = max(dp[j]+1,dp[i])
print(max(dp))