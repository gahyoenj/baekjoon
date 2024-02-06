n = int(input())
chang = 100
sang = 100
for round in range(n):
  c, s = map(int, input().split())
  if c > s:
    sang -= c
  elif c< s:
    chang -= s
  
print(chang,sang)