N = int(input())
house = []
for _ in range(N):
    R,G,B = map(int,input().split())
    house.append((R,G,B))

dp = [[0] * 3 for _ in range(N)]

for i in range(3):
    dp[0][i] = house[0][i]

for idx in range(1,N):
    dp[idx][0] = min(dp[idx-1][1]+house[idx][0], dp[idx-1][2]+house[idx][0])
    dp[idx][1] = min(dp[idx-1][0]+house[idx][1], dp[idx-1][2]+house[idx][1])
    dp[idx][2] = min(dp[idx-1][0] + house[idx][2], dp[idx-1][1] + house[idx][2])

print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2]))