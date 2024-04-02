def combi(k,s):
    if k == M:
        print(*result)
        return

    for i in range(s,N):
        result[k] = num[i]
        combi(k+1,i+1)

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = [-1] * M
combi(0,0)