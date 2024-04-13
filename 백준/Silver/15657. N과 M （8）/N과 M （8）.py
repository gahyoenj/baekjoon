def combi(k,s):
    if k == M:
        print(*result)
        return

    for i in range(s,N):
        result[k] = arr[i]
        combi(k+1,i)

N, M = map(int,input().split())
arr = list(map(int, input().split()))
result = [-1] * M
arr.sort()
combi(0,0)