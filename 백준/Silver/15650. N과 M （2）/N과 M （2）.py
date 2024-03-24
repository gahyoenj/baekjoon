def combination(k,start):
    if k == M:
        print(*result)
        return

    for i in range(start,N):
        result[k] = arr[i]
        combination(k+1,i+1)



N, M = map(int, input().split())
result = [-1] * M
arr = [i for i in range(1,N+1)]
combination(0,0)