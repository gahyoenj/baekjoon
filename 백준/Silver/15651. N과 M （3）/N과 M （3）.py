def perm(k):
    if k == M:
        print(*result[:M])
        return

    for i in range(1,N+1):
        result[k] = i
        perm(k+1)


N, M = map(int, input().split())

result = [-1] * (N+1)
perm(0)