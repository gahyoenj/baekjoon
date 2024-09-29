while True:
    n, m = map(float,input().split())
    N = int(n)

    if N == 0 and m == 0.00:
        break

    m = int(m*100)
    lst = []
    for _ in range(N):
        c,p = map(float,input().split())
        lst.append((int(c),int(p*100+0.5)))

    dp = [0] * 10001

    for i in range(1,m+1):
        for j in range(N):
            candy_c = lst[j][0]
            candy_m = lst[j][1]

            if i < candy_m:
                continue

            dp[i] = max(dp[i], dp[i-candy_m]+candy_c)
    print(dp[m])