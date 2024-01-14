N = int(input())
lst = list(map(int, input().split()))
maxV = -1000000
minV = 1000000
for idx in range(N):
  if maxV < lst[idx]:
    maxV = lst[idx]
  if minV > lst[idx]:
    minV = lst[idx]
print(minV, maxV)