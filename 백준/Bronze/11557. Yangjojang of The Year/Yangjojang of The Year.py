T = int(input())
for tc in range(T):
  N = int(input())
  maxV = 0
  for _ in range(N):
    S, L = input().split()
    L = int(L)
    if L > maxV:
      maxV = L
      maxS = S
  print(maxS)