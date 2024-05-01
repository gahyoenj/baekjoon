import sys
input = sys.stdin.readline
N,Q = map(int,input().split())

visited = [False] * (N+1)

for _ in range(Q):
    want = int(input())
    ans = 0
    land = want
    lst = []
    while land >=1:
        lst.append(land)
        land //= 2

    lst.sort()

    for i in lst:
        if visited[i]:
            ans = i
            break


    visited[want] = True
    print(ans)