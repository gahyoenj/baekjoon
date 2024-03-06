N,K = map(int,input().split())
lst = []
for _ in range(N):
    Ai = int(input())
    lst.append(Ai)
lst.sort(reverse=True)

cnt = 0
for idx in range(len(lst)):
    if K == 0:
        break
    if lst[idx] <= K:
        num = 0
        num = K // lst[idx]
        K -= num * lst[idx]
        cnt += num


print(cnt)