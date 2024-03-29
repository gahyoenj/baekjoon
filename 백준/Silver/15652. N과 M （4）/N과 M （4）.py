def combi(k,n):
    if n == M:
        print(*result)
        return

    for i in range(k,N+1):
        result[n] = i
        combi(i,n+1)

N,M = map(int, input().split())
result = [-1] * M
combi(1,0)