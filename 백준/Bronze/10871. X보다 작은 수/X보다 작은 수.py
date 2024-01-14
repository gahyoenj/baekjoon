N, X = map(int, input().split())
lst = list(map(int, input().split()))
for idx in range(N):
  if lst[idx] < X:
    print(lst[idx], end=' ')