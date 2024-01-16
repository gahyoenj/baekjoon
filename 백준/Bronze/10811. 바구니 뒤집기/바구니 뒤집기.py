N, M = map(int, input().split())
lst = list(range(1,N+1))
for idx in range(M):
  i, j =map(int, input().split())
  lst[i-1:j] = lst[i-1:j][::-1]
for basket in lst:
  print(basket,end=' ')