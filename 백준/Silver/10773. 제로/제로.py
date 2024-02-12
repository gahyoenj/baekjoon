K = int(input())
STACK = []
for _ in range(K):
  N = int(input())
  if N != 0:
    STACK.append(N)
  if N == 0:
    STACK.pop()
if STACK:
  print(sum(STACK))
else:
  print(0)