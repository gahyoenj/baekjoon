def combi(k):
    if k==M:
        print(*result)
        return

    for i in range(N):
        result[k] = arr[i]
        combi(k+1)

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [-1] * M
combi(0)