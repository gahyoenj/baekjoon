N = int(input())
lst = list(map(int, input().split()))
v = int(input())
idx = 0
cnt = 0
for idx in range (N):
  if lst[idx] == v:
    cnt = cnt + 1
print(cnt)