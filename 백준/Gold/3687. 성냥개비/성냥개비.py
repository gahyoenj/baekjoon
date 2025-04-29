matches = [6,2,5,5,4,5,6,3,7,6]

num = ['','',1,7,4,2,6,8]
dp = [2e19] * 101

for i in range(2,8):
    dp[i] = num[i]

T = int(input())
for _ in range(T):
    cnt = int(input())

    if cnt > 7:
        for i in range(8,cnt+1):
            for j in range(2,i-1):
                dp[i] = min(dp[i], int(str(dp[j])+str(dp[i-j])))
                if j == 6:
                    dp[i] = min(dp[i], int(str(dp[i-j])+'0'))

    minV = dp[cnt]

    maxV = '1' * (cnt//2)
    if cnt % 2 == 1:
        maxV = '7' + maxV[1:]

    print(minV, maxV)

