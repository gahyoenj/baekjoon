from itertools import combinations
def solution(n, money):
    answer = 0
    
    dp = [0] * (n+1)
    dp[0] = 1
    
    for coin in money:
        for i in range(coin,n+1):
            dp[i] = (dp[i] + dp[i-coin]) % 1000000007
    
    answer = dp[n]
    return answer