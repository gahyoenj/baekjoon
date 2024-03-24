def dfs(k,subSum):
    global ans
    if k == N:
        if subSum == S:
            ans += 1
        return

    dfs(k+1,subSum)
    dfs(k+1,subSum+arr[k])

N, S = map(int,input().split())
arr = list(map(int, input().split()))
if S != 0:
    ans = 0
else:
    ans = -1
dfs(0,0)
print(ans)